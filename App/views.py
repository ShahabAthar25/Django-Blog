from django.shortcuts import render

# Create your views here.

def home(request):
    properties = {}
    return render(request, 'App/home.html', properties)

def about(request):
    properties = {}
    return render(request, 'App/about.html', properties)

def FAQ(request):
    properties = {}
    return render(request, 'App/FAQ.html', properties)

def makepost(request):
    properties = {}
    return render(request, 'App/makepost.html', properties)

def profile(request):
    properties = {}
    return render(request, 'App/profile.html', properties)

def login(request):
    properties = {}
    return render(request, 'App/login.html', properties)

def signup(request):
    properties = {}
    return render(request, 'App/signup.html', properties)