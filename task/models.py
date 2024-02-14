from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


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
    short_description = RichTextField(blank=True, null=True)
    # short_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    category = models.CharField(max_length=200, default='uncategorized')
    snippet = models.CharField(max_length=200, default='Click on the link above to add a task.')
    completed = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='task_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} (Published by: '{self.author}' on {self.date_created})"

    def get_absolute_url(self):
        return reverse('home')
