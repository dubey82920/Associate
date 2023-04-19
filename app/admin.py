from django.contrib import admin

# Register your models her
from .models import Company,Employee
admin.site.register(Company)
admin.site.register(Employee)