# college_admin/views.py
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from college_admin.models import Department, Student


def admin_dashboard(request):
    departments = Department.objects.all()
    return render(request, 'college_admin/dashboard.html', {'departments': departments})

def user_logout(request):
    return redirect('users:login') 

def add_department(request):
    if request.method=='POST':
        department_name=request.POST.get('department_name')
        
        if department_name:
            Department.objects.create(name=department_name)
        return redirect('college_admin:dashboard')
        
    return render(request,'college_admin/add_department.html')    

def add_student(request):
    students = Student.objects.all()
    departments = Department.objects.all()  # Fetch all departments for dropdown

    if request.method == 'POST':
        admission_no = request.POST.get('admission_no')
        full_name = request.POST.get('full_name')
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
        )
        student.save()

        messages.success(request, 'Student added successfully!')
        return redirect('college_admin:add_student')

    return render(request, 'college_admin/admit_student.html', {'departments': departments, 'students': students})