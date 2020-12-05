from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, FAQ, aboutmodel

# Create your views here.

class home_view(ListView):
    model = Post
    template_name = 'App/home.html'

class about_view(ListView):
    model = aboutmodel
    template_name = 'App/about.html'

class FAQ_view(ListView):
    model = FAQ
    template_name = 'App/FAQ.html'

class make_post_view(ListView):
    model = Post
    template_name = 'App/make-post.html'

class profile_view(ListView):
    model = Post
    template_name = 'App/profile.html'

class login_view(ListView):
    model = Post
    template_name = 'App/login.html'

class sign_up_view(ListView):
    model = Post
    template_name = 'App/signup.html'