from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from college_admin.models import Student, Staff
from users.models import College


# Temporary Credentials for Each Role
USER_CREDENTIALS = {
    "teacher": {"username": "teacher", "password": "teacher123"},
    "librarian": {"username": "librarian", "password": "library123"},
    "accountant": {"username": "accountant", "password": "accountant123"},
    "department":{'username':'hod','password':'hod123'}
}

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        for role, creds in USER_CREDENTIALS.items():
            if username == creds["username"] and password == creds["password"]:
                if role == "teacher":
                    return redirect('teachers:dashboard')
                elif role == "librarian":
                    return redirect('library:dashboard')
                elif role == "accountant":
                    return redirect('accountant:dashboard')
                elif role == "department":
                    return redirect('department:dashboard')

        return render(request, 'users/login.html', {'error': 'Invalid Credentials'})

    return render(request, 'users/login.html')

def home(request):
    return render(request, 'users/home.html')


def college_register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        college_code = request.POST.get('college_code')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = make_password(request.POST.get('password'))  # Hash password

        if College.objects.filter(college_code=college_code).exists():
            messages.error(request, "College code already exists.")
            return redirect('users:college_register')

        if College.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('college_register')

        College.objects.create(
            full_name=full_name,
            college_code=college_code,
            email=email,
            phone=phone,
            password=password
        )
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('users:college_login')

    return render(request, 'users/college_register.html')

def college_login(request):
    if request.method == 'POST':
        college_code = request.POST.get('college_code')
        password = request.POST.get('password')

        try:
            college = College.objects.get(college_code=college_code)
            if check_password(password, college.password):
                # Store login state using session
                request.session['college_id'] = college.id
                request.session['college_code'] = college.college_code
                
                # ✅ Correctly redirect to the dashboard
                return redirect('college_admin:dashboard')  # Ensure this URL name exists in urls.py
            else:
                messages.error(request, "Invalid password.")
        except College.DoesNotExist:
            messages.error(request, "Invalid college code.")

    return render(request, 'users/college_login.html')  # Keep user on login page if auth fails


def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('users:home') 


def student_login(request):
    if request.method == "POST":
        admission_no = request.POST.get('admission_no')
        dob = request.POST.get('dob')

        try:
            student = Student.objects.get(admission_no=admission_no, dob=dob)
            request.session['student_id']=student.id
            request.session['student_name']=student.full_name

            messages.success(request,f'Welcome{student.full_name}!')
            return redirect('students:dashboard')
        
        except Student.DoesNotExist:
            messages.error(request, "Invalid Credentials")
            return redirect('users:student_login')

        # user, created = User.objects.get_or_create(username=student.admission_no, defaults={'first_name': student.full_name})
        # login(request, user)

        # messages.success(request, f"Welcome {student.full_name}!")
        

    return render(request, 'users/student_login.html')

def student_logout(request):
    logout(request)
    return redirect("users:student_login")

def staff_login(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        dob = request.POST.get('dob')

        try:
            staff = Staff.objects.get(staff_id=staff_id, dob=dob)
        except Staff.DoesNotExist:
            messages.error(request, "Invalid Credentials")
            return redirect('users:staff_login')

        return redirect('teachers:dashboard')
    
    return render(request, 'users/staff_login.html')
