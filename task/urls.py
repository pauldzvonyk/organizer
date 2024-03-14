from django.urls import path
from .views import (HomeView, TaskDetailView, AddTaskView, EditTaskView, DeleteTaskView, AddCategoryView, CategoryView,
                    LikeView, AddCommentView, landing_page)

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', HomeView.as_view(), name='home'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('task/edit/<int:pk>', EditTaskView.as_view(), name='edit_task'),
    path('task/delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('like/<int:pk>/', LikeView, name='like_task'),
    path('task/<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
]
