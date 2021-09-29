from django.db import models


# Create your models here.
class Employee(models.Model):
    emplyee_id = models.TextField(unique=True)
    emplyee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    employee_address = models.TextField()


# Create your models here.
