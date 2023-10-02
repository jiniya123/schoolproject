from django.db import models
from django.contrib.auth.models import User
  # Import Material model from the same module



# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)
    purpose = models.CharField(max_length=50)
    materials_provide = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name
