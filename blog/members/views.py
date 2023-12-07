from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView


class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangeForm
    #success_url= reverse_lazy('home')
    success_url= reverse_lazy('password_success')
    template_name='registration/change-password.html'

def password_success(request):
    return render(request, 'registration/change-password.html', {})


class UserRegisterView(generic.CreateView):
    form_class= SignupForm
    template_name='registration/register.html'
    success_url= reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('home')


    def get_object(self):
        return self.request.user

# Create your views here.
