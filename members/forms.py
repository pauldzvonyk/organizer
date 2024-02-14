from django.contrib.auth.forms import UserCreationForm
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