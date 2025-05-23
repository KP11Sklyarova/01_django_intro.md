from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)