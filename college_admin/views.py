# college_admin/views.py
from django.shortcuts import render,redirect
from college_admin.models import Department

def admin_dashboard(request):
    departments = Department.objects.all()

    return render(request, 'college_admin/dashboard.html', {'departments': departments})

def add_department(request):
    if request.method=='POST':
        department_name=request.POST.get('department_name')
        
        if department_name:
            Department.objects.create(name=department_name)
        return redirect('college_admin:dashboard')
        
    return render(request,'college_admin/add_department.html')    

