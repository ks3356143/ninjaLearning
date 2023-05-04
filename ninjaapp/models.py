from django.db import models

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(default=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey("auth.User", null=True, blank=True,on_delete=models.CASCADE)
