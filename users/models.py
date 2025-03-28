# Create your models here.
from django.db import models


class College(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    college_code = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)


