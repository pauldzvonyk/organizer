from django.urls import path
# from . import views
from .views import HomeView, TaskDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]
