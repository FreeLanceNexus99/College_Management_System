from django.db import models
from django.core.validators import MinLengthValidator
from users.models import College

class Department(models.Model):
    name=models.CharField(max_length=200)
    department_code = models.CharField(max_length=5, unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255) 

    def __str__(self):
        return self.name 

class Student(models.Model):

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    admission_no = models.CharField(max_length=4, unique=True)
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_no = models.PositiveIntegerField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    year_of_joining = models.PositiveIntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)

class Staff(models.Model):
    name = models.CharField(max_length=255)
    staff_id = models.CharField(max_length=4, unique=True, validators=[MinLengthValidator(4)])
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)