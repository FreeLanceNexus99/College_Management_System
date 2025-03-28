from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.urls import reverse
from django.contrib.auth.models import User
from college_admin.models import Student


# Temporary Credentials for Each Role
USER_CREDENTIALS = {
    "collegeadmin": {"username": "admin", "password": "admin123"},
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
                if role == "collegeadmin":
                    return redirect('college_admin:dashboard')
                elif role == "teacher":
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
    return render(request, 'users/college_register.html')

def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('users:home') 


def student_login(request):
    if request.method == "POST":
        admission_no = request.POST.get('admission_no')
        dob = request.POST.get('dob')

        try:
            student = Student.objects.get(admission_no=admission_no, dob=dob)
        except Student.DoesNot.Exist:
            messages.error(request, "Invalid Credentials")
            return redirect('users:student_login')

        # user, created = User.objects.get_or_create(username=student.admission_no, defaults={'first_name': student.full_name})
        # login(request, user)

        # messages.success(request, f"Welcome {student.full_name}!")
        return redirect("students:dashboard")

    return render(request, 'users/student_login.html')

def student_logout(request):
    logout(request)
    return redirect("users:student_login")