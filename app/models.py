from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    # other fields for company
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name