from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'context',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'username', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Content'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'context', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Title'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter The Post Content'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Enter The Post Content'}),
        }