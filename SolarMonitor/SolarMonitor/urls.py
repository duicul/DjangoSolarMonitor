"""
URL configuration for SolarMonitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # new
from django.views.generic.base import TemplateView  # new
import accounts.views
from accounts.views import MainView
from main.views import SensorListView, SensorValueListView, SensorCreateView,\
    SensorDeleteView
urlpatterns = [
    path('',MainView.as_view(),name="index"),
    path('logout/',accounts.views.logout_view),
    path("", include("django.contrib.auth.urls")),
    path("signup/",accounts.views.SignUpView.as_view(),name="signup"),
    path("changepassword/",accounts.views.change_password, name='change_password'),
    path("sensor/", SensorListView.as_view(), name="sensor-list"),
    path("sensor/<int:id>/", SensorValueListView.as_view(), name="sensor-value-list"),
    path("sensorcreate/",SensorCreateView.as_view(),name="sensor-create"),
    path("sensordelete/<int:pk>/",SensorDeleteView.as_view(),name="sensor-delete") #pk needed in url for deletion
    #path('admin/', admin.site.urls),
    #path('login/', main.views.login,name="login"),
    #path("accounts/", include("accounts.urls")),  # new
    #path("accounts/", include("django.contrib.auth.urls")),  # new
    #path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
]
