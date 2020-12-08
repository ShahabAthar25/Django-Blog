from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, FAQ, About
from .forms import Postform, EditPostForm
from django.urls import reverse_lazy

# Create your views here.

class home_view(ListView):
    model = Post
    template_name = 'App/home.html'
    ordering = ['-date_created']

class about_view(ListView):
    model = About
    template_name = 'App/about.html'

class FAQ_view(ListView):
    model = FAQ
    template_name = 'App/FAQ.html'

class make_post_view(CreateView):
    model = Post
    form_class = Postform
    template_name = 'App/make-post.html'
    #fields = '__all__'

class profile_view(ListView):
    model = Post
    template_name = 'App/profile.html'

class post_detail_view(DetailView):
    model = Post
    template_name = 'App/post-detail.html'

class post_edit_view(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'App/edit-post.html'

class delete_view(DeleteView):
    model = Post
    template_name = 'App/delete-post.html'
    success_url = reverse_lazy('home')

def CategoryView(request, cate):
    category_post = Post.objects.filter(category=cate.replace('-', ' '))
    return render(request, 'App/category.html', {'cate':cate, 'category_post':category_post})