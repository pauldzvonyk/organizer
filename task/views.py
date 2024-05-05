from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Comment
from .forms import TaskForm, EditForm, AddComment
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST


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
        cat_list = Task.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list

        unique_categories = set()
        user = self.request.user
        filtered_tasks = []

        for task in context['object_list']:
            if user.id == task.author.id:
                if task.category not in unique_categories:
                    unique_categories.add(task.category)
                    filtered_tasks.append(task)

        context['filtered_tasks'] = filtered_tasks

        task = self.get_task()

        progress_data = {
            0: {'text': "Define your goal clearly. Whether it's writing a novel, learning a new skill, or completing "
                        "a project, clarity is key.",
                'image_url': 'task/images/seed.png',
                'progress_bar': '<div class="progress-bar bg-secondary" role="progressbar" style="width: 100%" '
                                'aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%</div>',
                },
            1: {'text': "Break down your goal into smaller, manageable tasks. This makes it less overwhelming and "
                        "more achievable.",
                'image_url': 'task/images/tree01.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 10%" '
                                'aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">10%</div>',
                },
            2: {'text': "Create a timeline or schedule for completing each task. Setting deadlines helps keep you "
                        "accountable and on track.",
                'image_url': 'task/images/tree02.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 20%" '
                                'aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">20%</div>',
                },
            3: {'text': "Gather any necessary resources or materials needed to accomplish your goal. This might "
                        "include books, software, or other tools.",
                'image_url': 'task/images/tree03.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 30%" '
                                'aria-valuenow="30" aria-valuemin="0" aria-valuemax="100">30%</div>',
                },
            4: {'text': "Start with the first task on your list. Take that initial step forward, no matter how small "
                        "it may seem.",
                'image_url': 'task/images/tree04.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 40%" '
                                'aria-valuenow="40" aria-valuemin="0" aria-valuemax="100">40%</div>',
                },
            5: {'text': "Stay organized throughout the process. Keep track of your progress and adjust your plan as "
                        "needed.",
                'image_url': 'task/images/tree05.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 50%" '
                                'aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">50%</div>',
                },
            6: {'text': "Don't be afraid to ask for help if you get stuck. Seek guidance from friends, colleagues, "
                        "or online communities.",
                'image_url': 'task/images/tree06.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 60%" '
                                'aria-valuenow="60" aria-valuemin="0" aria-valuemax="100">60%</div>',
                },
            7: {'text': "Stay focused and motivated. Remind yourself why you're pursuing this goal and celebrate your "
                        "achievements along the way.",
                'image_url': 'task/images/tree07.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 70%" '
                                'aria-valuenow="70" aria-valuemin="0" aria-valuemax="100">70%</div>',
                },
            8: {'text': "Keep pushing forward, even when faced with challenges or setbacks. Perseverance is key to "
                        "reaching your goal.",
                'image_url': 'task/images/tree08.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 80%" '
                                'aria-valuenow="80" aria-valuemin="0" aria-valuemax="100">80%</div>',
                },
            9: {'text': "You're almost there, just one more push! Keep going until you've successfully completed your "
                        "task or achieved your goal. You can do it!",
                'image_url': 'task/images/tree09.PNG',
                'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 90%" '
                                'aria-valuenow="90" aria-valuemin="0" aria-valuemax="100">90%</div>',
                },
            10: {'text': "",
                 'image_url': 'task/images/tree10.PNG',
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


class AllTasksView(CategoryMixin, ListView):
    model = Task
    template_name = 'task/all_tasks.html'
    ordering = ['-date_created']


class TaskDetailView(CategoryMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


@require_POST
def increment_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.progress += 1

    # Extract subtask_text values directly from the request.POST data
    subtask_text_1 = request.POST.get('subtask_text_1')
    subtask_text_2 = request.POST.get('subtask_text_2')
    subtask_text_3 = request.POST.get('subtask_text_3')
    subtask_text_4 = request.POST.get('subtask_text_4')
    subtask_text_5 = request.POST.get('subtask_text_5')
    subtask_text_6 = request.POST.get('subtask_text_6')
    subtask_text_7 = request.POST.get('subtask_text_7')
    subtask_text_8 = request.POST.get('subtask_text_8')
    subtask_text_9 = request.POST.get('subtask_text_9')
    subtask_text_10 = request.POST.get('subtask_text_10')

    # Update the corresponding fields of the task object with the extracted values
    task.subtask_text_1 = subtask_text_1
    task.subtask_text_2 = subtask_text_2
    task.subtask_text_3 = subtask_text_3
    task.subtask_text_4 = subtask_text_4
    task.subtask_text_5 = subtask_text_5
    task.subtask_text_6 = subtask_text_6
    task.subtask_text_7 = subtask_text_7
    task.subtask_text_8 = subtask_text_8
    task.subtask_text_9 = subtask_text_9
    task.subtask_text_10 = subtask_text_10

    # Save the updated task object
    task.save()

    return redirect('task-detail', pk=pk)


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('all-tasks')

    # fields = '__all__'
    # fields = ('title', 'author', 'short_description', 'progress')


class AddCommentView(CreateView):
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
