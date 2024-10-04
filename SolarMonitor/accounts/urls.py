# accounts/urls.py
from django.urls import path

import accounts.views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/',LoginView.as_view()),
    
]
