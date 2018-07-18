from django.db import models


class Employee(models.Model):
    FirstName = models.CharField(max_length=100, blank=True, default='')
    MiddleInitial = models.CharField(max_length=100, blank=True, default='')
    LastName = models.CharField(max_length=100, blank=True, default='')
    DateOfBirth = models.DateField(blank=True)
    DateOfEmployment = models.DateField(blank=True)
    StatusBoolean = models.BooleanField(default=True)
