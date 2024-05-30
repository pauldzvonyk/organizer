from django.urls import path
from .views import UserRegistrationView, SettingsUpdateView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_settings/', SettingsUpdateView.as_view(), name='edit_settings'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password-change.html')),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='user_profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]

# urlpatterns = [
#     path('register/', UserRegistrationView.as_view(), name='register'),
#     path('edit_settings/', SettingsUpdateView.as_view(), name='edit_settings'),
#     path('password/', PasswordsChangeView.as_view(template_name='registration/password-change.html')),
#     path('<int:pk>/profile/', ProfilePageView.as_view(), name='user_profile'),
#     path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
#     path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
# ]

