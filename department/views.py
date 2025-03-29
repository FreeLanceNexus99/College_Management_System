from django.shortcuts import render, redirect
from college_admin.models import Department


def department_dashboard(request):
    department_id = request.session.get('department_id')

    if not department_id:
        messages.error(request, "You must log in first.")
        return redirect('users:department_login')  # Redirect to login if session is not set

    try:
        department = Department.objects.get(id=department_id)  # Fetch the department
        college = department.college  # Fetch the related college

    except Department.DoesNotExist:
        messages.error(request, "Department not found.")
        return redirect('users:department_login')

    return render(request, 'department/dashboard.html', {"department": department,"department_name": department.name,"college_name": college.full_name})


