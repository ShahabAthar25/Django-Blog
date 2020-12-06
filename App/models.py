from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    date_created = models.DateField(auto_now=True)

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