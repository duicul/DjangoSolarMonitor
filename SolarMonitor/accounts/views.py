# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
import json
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
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
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(SignUpView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login')
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def change_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })