#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . models import Task
from .forms import TaskForm, EditForm


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


class EditTaskView(UpdateView):
    model = Task
    form_class = EditForm
    # no need to define form_class, as it has already been taken care of with UpdateView
    template_name = 'task/edit_task.html'
    #fields = ('title', 'title_tag', 'short_description', 'date_created', 'priority', 'completed')
