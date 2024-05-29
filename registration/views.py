from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm, UserPasswordChangeForm
from django.contrib.auth import logout

# Create your views here.

class PasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class profile_view(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def logout_user(request):
    logout(request)
    
    return redirect("home")