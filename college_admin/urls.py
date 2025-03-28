from django.urls import path
from college_admin import views


app_name = 'college_admin'

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path("add-department/", views.add_department, name='add_department'),
    path("add-student/", views.add_student, name="add_student"),
    path('logout/', views.user_logout, name='logout'),
    path('add-staff/', views.add_staff, name='add_staff'),
    path('students/', views.student_list, name='student_list'),  # ✅ Ensure this path exists

]
