from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Temporary Credentials for Each Role
USER_CREDENTIALS = {
    "collegeadmin": {"username": "admin", "password": "admin123"},
    "teacher": {"username": "teacher", "password": "teacher123"},
    "student": {"username": "student", "password": "student123"},
    "librarian": {"username": "librarian", "password": "library123"},
    "accountant": {"username": "accountant", "password": "accountant123"},
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
                elif role == "student":
                    return redirect('students:dashboard')
                elif role == "librarian":
                    return redirect('library:dashboard')
                elif role == "accountant":
                    return redirect('accountant:dashboard')

        return render(request, 'users/login.html', {'error': 'Invalid Credentials'})

    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('users:login')
