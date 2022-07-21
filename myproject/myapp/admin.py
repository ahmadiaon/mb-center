from django.contrib import admin

from employee.models import Employee
from .models import Feature

# Register your models here.

admin.site.register(Feature)
admin.site.register(Employee)
