# students/views.py
from django.shortcuts import render, redirect
from college_admin.models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def student_dashboard(request):
    student_id = request.session.get('student_id')  # Get student ID from session

    if not student_id:
        return redirect('users:student_login')  # Redirect to login if session not set

    try:
        student = Student.objects.get(id=student_id)  # Fetch the student
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('users:student_login')

    return render(request, 'students/dashboard.html', {"student": student})

