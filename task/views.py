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

        task = self.get_task()

        progress_data = {
            0: {'text': 'Have an idea? Click on the link below and start a journey!',
                'image_url': 'task/images/seed.png',
                'progress_bar': '<div class="progress-bar bg-secondary" role="progressbar" style="width: 100%" '
                                'aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%</div>',
                },
            1: {'text': 'Text for case 1', 'image_url': 'task/images/tree01.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 10%" '
                                'aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">10%</div>',
                },
            2: {'text': 'Text for case 2', 'image_url': 'task/images/tree02.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 20%" '
                                'aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">20%</div>',
                },
            3: {'text': 'Text for case 3', 'image_url': 'task/images/tree03.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 30%" '
                                'aria-valuenow="30" aria-valuemin="0" aria-valuemax="100">30%</div>',
                },
            4: {'text': 'Text for case 4', 'image_url': 'task/images/tree04.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 40%" '
                                'aria-valuenow="40" aria-valuemin="0" aria-valuemax="100">40%</div>',
                },
            5: {'text': 'Text for case 5', 'image_url': 'task/images/tree05.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 50%" '
                                'aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">50%</div>',
                },
            6: {'text': 'Text for case 6', 'image_url': 'task/images/tree06.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 60%" '
                                'aria-valuenow="60" aria-valuemin="0" aria-valuemax="100">60%</div>',
                },
            7: {'text': 'Text for case 7', 'image_url': 'task/images/tree07.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 70%" '
                                'aria-valuenow="70" aria-valuemin="0" aria-valuemax="100">70%</div>',
                },
            8: {'text': 'Text for case 8', 'image_url': 'task/images/tree08.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 80%" '
                                'aria-valuenow="80" aria-valuemin="0" aria-valuemax="100">80%</div>',
                },
            9: {'text': 'Text for case 9', 'image_url': 'task/images/tree09.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 90%" '
                                'aria-valuenow="90" aria-valuemin="0" aria-valuemax="100">90%</div>',
                },
            10: {'text': 'Text for case 10', 'image_url': 'task/images/tree10.PNG',
                 'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 100%" '
                                 'aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">100%</div>',
                 },
        }

        current_progress_data = progress_data.get(task.progress, {})

        context['current_progress_data'] = current_progress_data

        # This part is only needed for DetailView Likes functionality
        # if hasattr(self, 'object'):
        #     db_likes = get_object_or_404(Task, id=self.object.pk)
        #     total_likes = db_likes.total_likes()
        #
        #     liked = False
        #     if db_likes.likes.filter(id=self.request.user.id).exists():
        #         liked = True
        #
        #     context['total_likes'] = total_likes
        #     context['liked'] = liked

        return context

    def get_task(self):
        if hasattr(self, 'object'):  # DetailView
            return self.object
        elif hasattr(self, 'get_queryset'):  # ListView
            queryset = self.get_queryset()
            return queryset.first() if queryset.exists() else None
        else:
            raise AttributeError("Cannot determine the type of view.")


class HomeView(CategoryMixin, ListView):
    model = Task
    template_name = 'task/all_tasks.html'
    ordering = ['-date_created']


class TaskDetailView(CategoryMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class AddTaskView(CategoryMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('all-tasks')
    # fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'progress')


class AddCategoryView(CategoryMixin, CreateView):
    model = Category
    template_name = 'task/add_category.html'
    fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'progress')


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

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['pk']})


class DeleteTaskView(CategoryMixin, DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = reverse_lazy('all-tasks')
