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
    image_header = models.ImageField(null=True, blank=True, upload_to='image_header/')
    task_images = models.ImageField(null=True, blank=True, upload_to='task_images/')
    short_description = RichTextField(blank=True, null=True)
    # short_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    category = models.CharField(max_length=200, default='uncategorized')
    snippet = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='task_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} (Published by: '{self.author}' on {self.date_created})"

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_image/')
    website_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    social_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.task.title, self.name)
