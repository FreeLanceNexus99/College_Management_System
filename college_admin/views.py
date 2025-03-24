# college_admin/views.py
from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'college_admin/dashboard.html')
