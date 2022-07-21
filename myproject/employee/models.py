from datetime import datetime
from turtle import update
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=500, null=True)
    photo_path = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    deleted_at = models.DateTimeField(default=datetime.now, blank=True)