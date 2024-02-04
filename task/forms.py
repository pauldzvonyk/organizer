from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'author', 'short_description', 'priority')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the task title...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter a short '
                                                                      'description of the '
                                                                      'task...'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
        }


"""
EditForm class is necessary to enable the form view with different widgets
"""
class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'title_tag', 'short_description', 'priority')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the task title...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter a short '
                                                                      'description of the '
                                                                      'task...'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
        }
