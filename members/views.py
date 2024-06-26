from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditSettingsForm, ChangePasswordForm, CreateProfileForm, EditProfileForm
from task.models import Profile, User
from django.contrib.auth.mixins import LoginRequiredMixin
from task.views import CategoryMixin


class CreateProfilePageView(CategoryMixin, CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile_page.html'
    success_url = reverse_lazy('home')

    """The form_valid function below adds the current user to the form and saves it."""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfilePageView(CategoryMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Fetch the user by pk provided in the URL and then get the profile
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        profile = get_object_or_404(Profile, user=user)
        return profile

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


class EditProfilePageView(CategoryMixin, LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile_page.html'

    def get_object(self, queryset=None):
        # Fetch the profile of the authenticated user
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        # Redirect to the user's profile page after successful form submission
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.pk})


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class SettingsUpdateView(CategoryMixin, generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('all-tasks')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/password-change.html'
    success_url = reverse_lazy('login')
