from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', UserRegisterView.as_view(), name='signup'),
    path('profile/', profile_view.as_view(), name='profile'),
    path('password/', PasswordChangeView.as_view(), name="password-change"),
    path('logout/', logout_user, name="logout-user"),
]
