from django.urls import path
from college_admin import views

app_name = 'college_admin'

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path("add-department/", views.add_department, name='add_department'),
]
