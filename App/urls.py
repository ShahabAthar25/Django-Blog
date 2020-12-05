from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_view.as_view()),
    path('about', about_view.as_view()),
    path('about/FAQ', FAQ_view.as_view()),
    path('make-post', make_post_view.as_view()),
    path('profile', profile_view.as_view()),
    path('login', login_view.as_view()),
    path('signup', sign_up_view.as_view()),
    path('post-detail/<int:pk>', post_detail_view.as_view(), name='post_detail'),
]