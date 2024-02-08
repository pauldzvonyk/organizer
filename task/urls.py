from django.urls import path
from .views import HomeView, TaskDetailView, AddTaskView, EditTaskView, DeleteTaskView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('task/edit/<int:pk>', EditTaskView.as_view(), name='edit_task'),
    path('task/delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
]
