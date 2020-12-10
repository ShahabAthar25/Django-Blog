from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign-up/', UserRegisterView.as_view(), name='signup'),
    path('profile/', profile_view.as_view(), name='profile'),
    path('password/', PasswordChangeView.as_view()),
]
