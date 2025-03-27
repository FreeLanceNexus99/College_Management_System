from django.urls import path
from .views import user_login, user_logout, student_login

app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('student-login/', student_login, name='student-login'),
    
]
