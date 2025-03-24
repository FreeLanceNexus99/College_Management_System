# library/views.py
from django.shortcuts import render

def librarian_dashboard(request):
    return render(request, 'library/dashboard.html')
