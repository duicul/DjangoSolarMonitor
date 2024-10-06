from django.db import models
from django.core.validators import URLValidator

SENSOR_TYPES = ["OneWire","WeatherAPI","DCVoltage"]

class Sensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 100, unique=True)
    host = models.CharField(max_length = 100,validators = [URLValidator()])
    unit = models.CharField(max_length = 100,default="C")
    sensor_type = models.CharField(max_length = 100,default="OneWire")
    key = models.CharField(max_length = 100,default="")
    def getDict(self):
        return {"id":self.id,"name":self.name,"ip_location":self.ip_location,"unit":self.unit}

class SensorValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensor =  models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    
    def getDict(self):
        return {"id":self.id,"sensor":self.sensor,"value":self.value,"timestamp":self.timestamp}

class Inverter(models.Model):
    id = models.BigAutoField(primary_key=True)
    host = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100, unique=True)
    pass

class PZMValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    inverter =  models.ForeignKey(Inverter, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    pass

class PowlandValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    inverter =  models.ForeignKey(Inverter, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    pass