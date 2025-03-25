from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),  # Authentication URLs
    path('college_admin/', include('college_admin.urls')),  # Admin Dashboard
    path('teachers/', include('teachers.urls')),  # Teacher Dashboard
    path('students/', include('students.urls')),  # Student Dashboard
    path('library/', include('library.urls')),  # Library Dashboard
    path('accountant/', include('accountant.urls')),  # Accountant Dashboard
]

