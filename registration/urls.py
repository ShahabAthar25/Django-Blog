from django.urls import path, include
from .views import *

urlpatterns = [
    path('sign-up/', UserRegisterView.as_view(), name='signup'),
    path('/profile/', profile_view.as_view()),
]
