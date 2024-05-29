from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view.as_view(), name='home'),
    path('about', about_view.as_view()),
    path('about/FAQ', FAQ_view.as_view()),
    path('make-post', make_post_view.as_view()),
    path('post-detail/<int:pk>', post_detail_view.as_view(), name='post_detail'),
    path('edit-detail/edit/<int:pk>', post_edit_view.as_view(), name='post_edit'),
    path('delete-detail/<int:pk>/delete', delete_view.as_view(), name='post_delete'),
    path('post/category/<str:cate>', CategoryView, name='post_category'),
    path('post/like/<int:pk>', LikeView, name='like_post'),
]