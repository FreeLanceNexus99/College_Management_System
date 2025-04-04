# college_admin/views.py
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from college_admin.models import Department, Student, Staff
from django.contrib.auth.hashers import make_password
from users.models import College
from django.core.mail import send_mail
from django.conf import settings


def admin_dashboard(request):
    college_id = request.session.get('college_id')  # Get logged-in college ID from session

    if not college_id:
        return redirect('users:college_login')  # Redirect to login if no session exists

    try:
        college = College.objects.get(id=college_id)  # Fetch the specific college
    except College.DoesNotExist:
        messages.error(request, "College not found.")
        return redirect('users:college_login')

    departments = Department.objects.filter(college=college)

    return render(request, 'college_admin/dashboard.html', {'departments': departments, 'college': college})

def student_list(request):
    college_id=request.session.get('college_id')
    
    if not college_id:
        return redirect('users:college_login')
    
    try:
        college=College.objects.get(id=college_id)

    except College.DoesNotExist:
        messages.error(request,'College not found') 
        return redirect('users:college_login')   
    
       
    students = Student.objects.filter(college=college)  
    return render(request, 'college_admin/student_list.html', {'students': students})


def user_logout(request):
    return redirect('users:login') 

def add_department(request):
    college_id = request.session.get('college_id')  # ✅ Get the logged-in college ID
    
    if not college_id:
        messages.error(request, "Please log in first.")
        return redirect('users:college_login')  # ✅ Redirect to login if not authenticated

    try:
        college = College.objects.get(id=college_id)  # ✅ Fetch the logged-in college
    except College.DoesNotExist:
        messages.error(request, "College not found.")
        return redirect('users:college_login')

    if request.method == 'POST':
        department_name = request.POST.get('department_name')

        if department_name:
            # ✅ Assign department to the logged-in college
            Department.objects.create(name=department_name, college=college)
            messages.success(request, "Department added successfully!")
            return redirect('college_admin:dashboard')  # ✅ Redirect to dashboard

        messages.error(request, "Department name cannot be empty.")

    return render(request, 'college_admin/add_department.html')  

def add_student(request):

    departments = Department.objects.all()  # Fetch all departments for dropdown
    college_id = request.session.get('college_id')
    if not college_id:
        messages.error(request, "Session expired. Please login in again.")
        return redirect("users:college_login")

    try:
        college = College.objects.get(id=college_id)
    except College.DoesNotExist:
        messages.error(request, "Session expired. Please log in again.")
        return redirect("users:college_login")


    if request.method == 'POST':
        admission_no = request.POST.get('admission_no')
        full_name = request.POST.get('full_name').title()
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone')
        department_id = request.POST.get('department')
        gender = request.POST.get('gender')
        year_of_joining = request.POST.get('year_of_joining')

        if not all([admission_no, full_name, dob, address, email, phone_no, department_id, gender, year_of_joining]):
            messages.error(request, "All fields are required.")
            return redirect("college_admin:add_student")

        if Student.objects.filter(admission_no=admission_no).exists():
            messages.error(request, "A student with this admission number already exists.")
            return redirect('college_admin:add_student')

        # ✅ Check if the department exists
        if Department.objects.filter(id=department_id).exists():
            department = Department.objects.get(id=department_id)
        else:
            messages.error(request, "Invalid department selection.")
            return redirect("college_admin:add_student")

        # ✅ Generate password using logged-in admin's college_code
        raw_password = f"{full_name.split()[0]}@{college.college_code}{admission_no}".lower()

        hashed_password = make_password(raw_password)


        # ✅ Create and save the student
        student = Student(
            admission_no=admission_no,
            full_name=full_name,
            dob=dob,
            address=address,
            email=email,
            phone_no=phone_no,
            department=department,
            gender=gender,
            year_of_joining=int(year_of_joining),
            college=college,
            password=hashed_password,
        )
        student.save()
        
        # ✅ Send email with credentials
        subject = "Welcome to Your College Portal"
        message = f"Dear {full_name},\n\nYour Student account has been created.\nLogin credentials:\nAdmission No: {admission_no}\nPassword: {raw_password}\n."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

        messages.success(request, 'Student added successfully! Login details sent to email.')
        return redirect('college_admin:add_student')


    return render(request, 'college_admin/admit_student.html', {'departments': departments})

def add_staff(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        staff_id = request.POST.get('staff_id')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        department_id = request.POST.get('department')

        if not all([name, staff_id, dob, gender, email, phone_no, address, department_id]):
            messages.error(request, 'All fields are required.')
            return redirect('college_admin:add_staff')

        if len(staff_id) != 4 or not staff_id.isdigit():
            messages.error(request, "Staff ID need to be in $ digits.")
            return redirect('college_admin:add_staff')
        
        if Staff.objects.filter(staff_id=staff_id).exists():
            messages.error(request, "A Staff member with this ID already exists.")
            return redirect("college_admin:add_staff")

        if not Department.objects.filter(id=department_id).exists():
            messages.error(request, "invalid department selected.")
            return redirect("college_admin:add_staff")
        
        department = Department.objects.get(id=department_id)

        staff = Staff(
            name=name,
            staff_id=staff_id,
            dob=dob,
            gender=gender,
            email=email,
            phone_no=phone_no,
            address=address,
            department=department,
        )
        staff.save()

        messages.success(request, "staff member added successfully!")
        return redirect("college_admin:add_staff")

    departments = Department.objects.all()
    return render(request, "college_admin/admit_staff.html", {'departments': departments})