from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Task, Comment
from .forms import TaskForm, EditForm, AddComment, EditCommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST


"""
   CategoryMixin -> DYNAMIC navbar category dropdown menu + AddTask & EditTask category choice.
   ProgressMixin -> DYNAMIC progress_data assignment in AllTasks & TaskDetail views
"""


class ProgressMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        task = self.get_task()
        if task:
            progress_data = {
                0: {
                    'text': "Define your goal clearly. Whether it's writing a novel, learning a new skill, "
                            "or completing a project, clarity is key.",
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
                4: {
                    'text': "Start with the first task on your list. Take that initial step forward, no matter how small "
                            "it may seem.",
                    'image_url': 'task/images/tree04.PNG',
                    'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 40%" '
                                    'aria-valuenow="40" aria-valuemin="0" aria-valuemax="100">40%</div>',
                    },
                5: {
                    'text': "Stay organized throughout the process. Keep track of your progress and adjust your plan as "
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
                7: {
                    'text': "Stay focused and motivated. Remind yourself why you're pursuing this goal and celebrate your "
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
                9: {
                    'text': "You're almost there, just one more push! Keep going until you've successfully completed your "
                            "task or achieved your goal. You can do it!",
                    'image_url': 'task/images/tree09.PNG',
                    'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 90%" '
                                    'aria-valuenow="90" aria-valuemin="0" aria-valuemax="100">90%</div>',
                },
                10: {'text': "You have successfully accomplished your Task, I am really proud of you, but you "
                             "shouldn't waste time, set your new Task and move to your new objective!",
                     'image_url': 'task/images/tree10.PNG',
                     'progress_bar': '<div class="progress-bar bg-success" role="progressbar" style="width: 100%" '
                                     'aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">100%</div>',
                     },
            }

            current_progress_data = progress_data.get(task.progress, {})

            context['current_progress_data'] = current_progress_data
        return context


class CategoryMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        cat_list = Task.objects.all()
        if cat_list.exists():
            context['cat_list'] = cat_list

        if self.request.user.is_authenticated:
            user_tasks = Task.objects.filter(author=self.request.user)
            categories = user_tasks.order_by('category').values_list('category', flat=True).distinct()
            context['categories'] = categories

            user_task_count = user_tasks.count()
            context['user_task_count'] = user_task_count

        return context

    def get_task(self):
        if hasattr(self, 'object'):  # DetailView
            return self.object
        elif hasattr(self, 'get_queryset'):  # ListView
            queryset = self.get_queryset()
            return queryset.first() if queryset.exists() else None
        else:
            raise AttributeError("Cannot determine the type of view.")


class LandingPageView(CategoryMixin, TemplateView):
    template_name = 'task/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = 'pauldzvonyk81@gmail.com'
        return context


class SearchTaskView(CategoryMixin, TemplateView):
    def post(self, request):
        searched = request.POST.get('search-for')
        all_searched = Task.objects.filter(title__icontains=searched)
        context = {'searched': searched, 'all_searched': all_searched}
        context.update(self.get_context_data())
        return render(request, 'task/search_task.html', context=context)

    def get(self, request):
        context = self.get_context_data()
        return render(request, 'task/search_task.html', context=context)


class AllTasksView(ProgressMixin, CategoryMixin, ListView):
    model = Task
    template_name = 'task/all_tasks.html'
    ordering = ['-date_created']


class TaskDetailView(ProgressMixin, CategoryMixin, DetailView):
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

    if task.progress >= 10:
        return redirect('task-completed', pk=pk)

    return redirect('task-detail', pk=pk)


class AddTaskView(CategoryMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('all-tasks')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    # fields = '__all__'
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


class EditCommentView(CategoryMixin, UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'task/edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['task_pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.get(pk=self.kwargs['task_pk'])
        context['task'] = task
        context['user'] = self.request.user
        return context


class DeleteCommentView(CategoryMixin, DeleteView):
    model = Comment
    template_name = 'task/delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.task_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=self.object.task_id)
        context['task'] = task
        return context


class CategoryView(ProgressMixin, CategoryMixin, ListView):
    model = Task
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
    template_name = 'task/edit_task.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs


class DeleteTaskView(CategoryMixin, DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = reverse_lazy('all-tasks')


class TaskCompletedView(CategoryMixin, DetailView):
    model = Task
    template_name = 'task/task_completed.html'
