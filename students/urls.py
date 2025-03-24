from django.urls import path
from .views import student_dashboard

app_name = 'students'

urlpatterns = [
    path('dashboard/', student_dashboard, name='dashboard'),
]
