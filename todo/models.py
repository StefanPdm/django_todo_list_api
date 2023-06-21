from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo (models.Model):
  title = models.CharField(max_length=200, null=True)
  description = models.CharField(max_length=200, null=True, blank=True)  
  created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
  completed = models.BooleanField(default=False, null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)