from django.shortcuts import render

def department_dashboard(request):
    return render(request,'department/dashboard.html')
