from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(timezone.now())
