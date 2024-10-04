# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import logout
import json
from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView

class MainView(TemplateView):
    template_name = "index.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(MainView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login')# render(request,LoginView.as_view())#  super(HomeView, self).dispatch(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")