from django.urls import path
from department import views

app_name = 'department'


urlpatterns=[
    path('dashboard/',views.department_dashboard,name='dashboard'),
]