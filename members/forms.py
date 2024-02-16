from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

"""Customizing the registration form, adding extra fields like email, name, surname etc...
    built in UserCreationForm is instantiated with default fields (username, password1 and password2),
    taking care of all the logic to handle password authentication. To extend the fields, we need to use 
    __init__ method inside Meta class, and pass bootstrap classes to modify built in fields. Additional
    fields can be bootstrapped directly by passing them as variables in SignUpForm.    
    """


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


"""No need to override the __init__ method in this case, because we don't add new fields to the Edit Profile form,
   but only bootstrap existing ones, defining the order of appearance in Meta class"""


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login',
                  'date_joined', 'is_superuser', 'is_staff', 'is_active')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=50,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=50,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
