from django import forms
from .models import Post
from datetime import datetime

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'context', 'date_created',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Content'}),
            'date_created': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date Like This: Year-Month-Day'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'context')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Title'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Content'}),
        }