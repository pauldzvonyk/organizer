from django.urls import path
from .views import UserRegistrationView, ProfileUpdateView, PasswordsChangeView, ProfilePageView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password-change.html')),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='user_profile'),
]

