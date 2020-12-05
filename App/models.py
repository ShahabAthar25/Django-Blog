from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    date_created = models.DateField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class FAQ(models.Model):
    question = models.CharField(max_length=60)
    Answer = models.TextField()

    def __str__(self):
        return self.question

class aboutmodel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title