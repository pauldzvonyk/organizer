from django.contrib import admin
from .models import Task, Category, Profile, Comment

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
