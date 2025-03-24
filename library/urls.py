from django.urls import path
from .views import librarian_dashboard

app_name = 'library'

urlpatterns = [
    path('dashboard/', librarian_dashboard, name='dashboard'),
]
