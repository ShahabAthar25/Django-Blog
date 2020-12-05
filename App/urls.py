from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('about/FAQ', views.FAQ),
    path('makepost', views.makepost),
    path('profile', views.profile),
    path('login', views.login),
    path('signp', views.signup),
]