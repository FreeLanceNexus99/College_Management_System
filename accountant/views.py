# accountant/views.py
from django.shortcuts import render

def accountant_dashboard(request):
    return render(request, 'accountant/dashboard.html')
