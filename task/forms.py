from django import forms
from .models import Task, Category

# hard-coded variable assignment syntax and django format
# choice = [('work', 'work'), ('sport', 'sport'), ('family', 'family')]
choice_list = Category.objects.all().values_list('category_name', 'category_name')

choice = []

for item in choice_list:
    choice.append(item)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'author', 'category', 'short_description', 'priority')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'js_tweek_id', 'type': 'hidden'}),
            'category': forms.Select(choices=choice, attrs={'class': 'form-control'}),
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
        fields = ('title', 'category', 'short_description', 'priority')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the task title...'}),
            'category': forms.Select(choices=choice, attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter a short '
                                                                      'description of the '
                                                                      'task...'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
        }
