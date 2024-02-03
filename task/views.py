#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Task
from .forms import TaskForm


# def home(request):
#     return render(request, 'task/home.html', {})

class HomeView(ListView):
    model = Task
    template_name = 'task/home.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'

class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    # fields = '__all__'
    #fields = ('title', 'author', 'short_description', 'priority')
