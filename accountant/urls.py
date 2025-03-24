from django.urls import path
from .views import accountant_dashboard

app_name = 'accountant'

urlpatterns = [
    path('dashboard/', accountant_dashboard, name='dashboard'),
]
