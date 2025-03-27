from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=200)



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