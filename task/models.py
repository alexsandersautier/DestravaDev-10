from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=1)