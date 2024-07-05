from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('sign_in')
    template_name = 'sign_up.html'
    
class SignIn(LoginView):
    template_name = 'sign_in.html'
    next_page = reverse_lazy('home')
    
class LogOut(LogoutView):
    next_page = reverse_lazy('sign_in')
    
def home(request):
    return render(request, 'home.html')