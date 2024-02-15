from django.urls import path
from .views import UserRegistrationView, ProfileUpdateView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
]

