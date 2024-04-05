from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category, Comment
from .forms import TaskForm, EditForm, AddComment
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


def landing_page(request):
    return render(request, 'task/home.html')


def search_task(request):
    if request.method == 'POST':
        searched = request.POST['search-for']
        all_searched = Task.objects.filter(title__contains=searched)
        return render(request, 'task/search_task.html',
                      {'searched': searched, 'all_searched': all_searched})
    else:
        return render(request, 'task/search_task.html')



def LikeView(request, pk):
    task = get_object_or_404(Task, id=request.POST.get('task_id'))
    liked = False
    if task.likes.filter(id=request.user.id).exists():
        task.likes.remove(request.user)
        liked = False
    else:
        task.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('task-detail', args=[str(pk)]))


"""CategoryMixin class is necessary to view DYNAMIC category dropdown menu in a navbar"""


class CategoryMixin:
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context


class HomeView(CategoryMixin, ListView):
    model = Task
    template_name = 'task/all_tasks.html'
    ordering = ['-date_created']


class TaskDetailView(CategoryMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        db_likes = get_object_or_404(Task, id=self.kwargs['pk'])
        total_likes = db_likes.total_likes()

        liked = False
        if db_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddTaskView(CategoryMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('all-tasks')
    # fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'priority')


class AddCategoryView(CategoryMixin, CreateView):
    model = Category
    template_name = 'task/add_category.html'
    fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'priority')


class AddCommentView(CategoryMixin, CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'task/add_comment.html'

    def form_valid(self, form):
        form.instance.task_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.get(pk=self.kwargs['pk'])
        context['task'] = task
        return context


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
    success_url = reverse_lazy('all-tasks')
