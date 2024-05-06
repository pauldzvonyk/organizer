from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    new_category = forms.CharField(max_length=200, required=False, label='New Category')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the current user from the kwargs
        super(TaskForm, self).__init__(*args, **kwargs)
        # Filter categories based on the current user's tasks
        categories = Task.objects.filter(author=user).order_by('category').values_list('category', flat=True).distinct()
        # Create a list of tuples for choices, including the default value and existing categories
        category_choices = [(category, category) for category in categories]
        # If 'uncategorized' is not already in the list, include it
        if 'uncategorized' not in categories:
            category_choices.insert(0, ('uncategorized', 'Uncategorized'))
        # Set the choices for the category field
        self.fields['category'].widget.choices = category_choices

    def clean(self):
        cleaned_data = super().clean()
        new_category = cleaned_data.get('new_category')
        if new_category:
            # If a new category is provided, use it instead of the existing category field
            cleaned_data['category'] = new_category
        return cleaned_data

    class Meta:
        model = Task
        fields = ('title', 'author', 'snippet', 'category', 'new_category', 'image_header',
                  'short_description', 'task_images', 'progress')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'js_tweak_id', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'new_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new category'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'progress': forms.TextInput(attrs={'class': 'form-control'}),
        }


"""
EditForm class is necessary to enable the form view with different widgets
"""
class EditForm(forms.ModelForm):
    new_category = forms.CharField(max_length=200, required=False, label='New Category')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the current user from the kwargs
        super(EditForm, self).__init__(*args, **kwargs)
        # Filter categories based on the current user's tasks
        categories = Task.objects.filter(author=user).order_by('category').values_list('category', flat=True).distinct()
        # Create a list of tuples for choices, including the default value and existing categories
        category_choices = [(category, category) for category in categories]
        # If 'uncategorized' is not already in the list, include it
        if 'uncategorized' not in categories:
            category_choices.insert(0, ('uncategorized', 'Uncategorized'))
        # Set the choices for the category field
        self.fields['category'].widget.choices = category_choices

    def clean(self):
        cleaned_data = super().clean()
        new_category = cleaned_data.get('new_category')
        if new_category:
            # If a new category is provided, use it instead of the existing category field
            cleaned_data['category'] = new_category
        return cleaned_data

    class Meta:
        model = Task
        fields = ('title', 'snippet', 'category', 'new_category', 'image_header', 'short_description', 'task_images', 'progress')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the task title...'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'new_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new category'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'progress': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
