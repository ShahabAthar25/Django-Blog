from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, FAQ, About
from .forms import Postform, EditPostForm
from django.urls import reverse_lazy

# Create your views here.

class login_view(ListView):
    model = Post
    template_name = 'App/login.html'

class sign_up_view(ListView):
    model = Post
    template_name = 'App/signup.html'