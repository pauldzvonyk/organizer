from django.urls import path
from .views import (AllTasksView, TaskDetailView, AddTaskView, EditTaskView, DeleteTaskView, AddCategoryView, CategoryView,
                    LikeView, AddCommentView, landing_page, search_task, increment_progress)

urlpatterns = [
    path('', landing_page, name='home'),
    path('search_task', search_task, name='search-task'),
    path('all_tasks/', AllTasksView.as_view(), name='all-tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/increment-progress/', increment_progress, name='increment-progress'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('task/edit/<int:pk>', EditTaskView.as_view(), name='edit_task'),
    path('task/delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('like/<int:pk>/', LikeView, name='like_task'),
    path('task/<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
]
