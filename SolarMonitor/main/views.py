import logging
from django.http.response import HttpResponseRedirect,HttpResponse
from accounts.views import MainView
from django.core.exceptions import ValidationError
logger = logging.getLogger("django")
from main.LoginForm import LoginForm
import hashlib
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from main.models import Sensor, SensorValue, SENSOR_TYPES
from django import forms
from django.forms import ModelForm
from .models import Sensor

class SensorListView(ListView):
    model = Sensor
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class SensorValueListView(TemplateView):
    template_name = "main/sensorvalue_list.html"
    def dispatch(self, request, *args, **kwargs):
        if "id" in kwargs :
            #SensorValue.objects.filter(sensor = id)
            self.sensorvalues = SensorValue.objects.filter(sensor__id = kwargs["id"])
            return super(SensorValueListView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/sensor')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sensorvalues"] = self.sensorvalues
        return context    

class SensorCreateForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ["name", "host", "unit","sensor_type","key"]
    
    

class SensorCreateView(CreateView):
    form_class = SensorCreateForm
    success_url = reverse_lazy("sensor-list")
    template_name = "main/sensor_create.html"
    sensor_types = SENSOR_TYPES
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sensor_types"] = self.sensor_types
        return context 

class SensorDeleteView(DeleteView):
    model = Sensor
    success_url = reverse_lazy("sensor-list") 
    
"""def index(request):
    username=None
    login=None
    try:
        username=request.session['username']
    except KeyError:
        username=None
    try:
        login=request.GET.get("login")
    except KeyError:
        login=None
    #print(username)
    if(username==None):
        return render(request,"index.html",{"login":login})
    return render(request,"index.html",{"login":login})
    return HttpResponse(json.dumps(["logged in"]), content_type="application/json")
    
def login(request):
    logger.info("utils.login "+str(request))
    username=None
    password=None
    MyLoginForm=None
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
    elif request.method == 'GET':
        MyLoginForm = LoginForm(request.GET)
    if MyLoginForm.is_valid() and not MyLoginForm == None:
        username = MyLoginForm.cleaned_data["username"]
        password = MyLoginForm.cleaned_data["password"]
    if not ( username == None or password == None):
        text_pass = hashlib.sha512(password.encode())
        encrypt_pass = text_pass.hexdigest()
        user_db=User_db.objects.filter(username = username)
        print("user_db "+str(user_db))
        if len(user_db)>0 and encrypt_pass == user_db[0].password:
            request.session['username']=username
            return  HttpResponseRedirect("/")
    return HttpResponseRedirect("/")"""
