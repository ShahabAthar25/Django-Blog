from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    context = RichTextField(blank=True, null=True)
    date_created = models.DateField(auto_now=True)
    category = models.CharField(max_length=30, default='Python')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_like(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

class FAQ(models.Model):
    question = models.CharField(max_length=60)
    Answer = models.TextField()

    def __str__(self):
        return self.question

class About(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.title