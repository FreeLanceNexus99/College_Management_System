# Create your models here.
from django.db import models

class CollegeAdmin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Temporary credentials

class Teacher(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Librarian(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Accountant(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
