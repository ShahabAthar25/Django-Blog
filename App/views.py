from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, FAQ, About, Category
from .forms import Postform, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

class home_view(ListView):
    model = Post
    template_name = 'App/home.html'
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(home_view, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context

class about_view(ListView):
    model = About
    template_name = 'App/about.html'

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(about_view, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context

class FAQ_view(ListView):
    model = FAQ
    template_name = 'App/FAQ.html'

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(FAQ_view, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context

class make_post_view(CreateView):
    model = Post
    form_class = Postform
    template_name = 'App/make-post.html'
    #fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(make_post_view, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context

class post_detail_view(DetailView):
    model = Post
    template_name = 'App/post-detail.html'

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(post_detail_view, self).get_context_data(*args, **kwargs)

        databasecheck = get_object_or_404(Post, id=self.kwargs['pk'])
        total_like = databasecheck.total_like()
        liked = False
        if databasecheck.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cate_menu'] = cate_menu
        context['total_like'] = total_like
        context['liked'] = liked

        return context

class post_edit_view(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'App/edit-post.html'

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(post_edit_view, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context

class delete_view(DeleteView):
    model = Post
    template_name = 'App/delete-post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(delete_view, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        return context

def CategoryView(request, cate):
    category_post = Post.objects.filter(category=cate)
    cate_menu = Category.objects.all()
    return render(request, 'App/category.html', {'cate':cate, 'category_post':category_post, 'cate_menu':cate_menu})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))