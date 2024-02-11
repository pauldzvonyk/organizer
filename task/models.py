from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('home')


class Task(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    category = models.CharField(max_length=200, default='uncategorized')
    completed = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='task_likes')

    def __str__(self):
        return f"{self.title} (Published by: '{self.author}' on {self.date_created})"

    def get_absolute_url(self):
        return reverse('home')

