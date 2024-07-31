from django.db import models

# Create your models here.
class Employee_Details(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Designation = models.CharField(max_length=200)
    Salary = models.IntegerField()

    def __str__(self):
        return self.First_Name
