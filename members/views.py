from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from task.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Use the authenticated user's profile for editing
        return self.request.user.profile


class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)

        current_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['current_user'] = current_user
        return context


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileUpdateView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/password-change.html'
    success_url = reverse_lazy('login')
