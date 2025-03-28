from django.urls import path
from .views import user_login, user_logout, student_login,home,college_register

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),  # Home page (Login form)
    path('register/', college_register, name='college_register'), 

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('student-login/', student_login, name='student-login'),
    
]
