from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Task


# def home(request):
#     return render(request, 'task/home.html', {})

class HomeView(ListView):
    model = Task
    template_name = 'task/home.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'

