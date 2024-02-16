from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm


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
    #form_class = PasswordChangeForm
    form_class = ChangePasswordForm
    template_name = 'registration/password-change.html'
    success_url = reverse_lazy('login')
