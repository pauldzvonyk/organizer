from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category
from .forms import TaskForm, EditForm
from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'task/home.html', {})


class CategoryMixin:
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context


class HomeView(CategoryMixin, ListView):
    model = Task
    template_name = 'task/home.html'
    ordering = ['-date_created']


class TaskDetailView(CategoryMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class AddTaskView(CategoryMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'priority')


class AddCategoryView(CategoryMixin, CreateView):
    model = Category
    template_name = 'task/add_category.html'
    fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'priority')


class CategoryView(CategoryMixin, ListView):
    template_name = 'task/categories.html'
    context_object_name = 'category_tasks'

    def get_queryset(self):
        cats = self.kwargs['cats']
        return Task.objects.filter(category=cats.replace('-', ' '))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = self.kwargs['cats']
        context['cats'] = cats.title().replace('-', ' ')
        return context


class EditTaskView(CategoryMixin, UpdateView):
    model = Task
    form_class = EditForm
    # no need to define form_class, as it has already been taken care of with UpdateView
    template_name = 'task/edit_task.html'
    # fields = ('title', 'title_tag', 'short_description', 'date_created', 'priority', 'completed')


class DeleteTaskView(CategoryMixin, DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = reverse_lazy('home')
