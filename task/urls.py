from django.urls import path
# from . import views
from .views import HomeView, TaskDetailView, AddTaskView, EditTaskView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('task/edit/<int:pk>', EditTaskView.as_view(), name='edit_task'),
]
