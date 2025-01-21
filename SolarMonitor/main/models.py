from django.db import models
from django.core.validators import URLValidator

SENSOR_TYPES = ["OneWire","WeatherAPI","DCVoltage"]
INVERTER_TYPES = ["POWLAND","PZM"]

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
    host = models.CharField(max_length = 100,validators = [URLValidator()])
    name = models.CharField(max_length = 100, unique=True)
    type = models.CharField(max_length = 100,default = "POWLAND")
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
    duration = models.IntegerField()
    OperationMode = models.IntegerField()
    EffectiveMainsVoltage = models.FloatField()
    MainsFrequency = models.FloatField()
    AverageMainsPower = models.FloatField()
    EffectiveInverterVoltage = models.FloatField()
    EffectiveInverterCurrent = models.FloatField()
    InverterFrequency = models.FloatField()
    AverageInverterPower = models.FloatField()
    InverterChargingPower = models.FloatField()
    OutputEffectiveVoltage = models.FloatField()
    OutputEffectiveCurrent = models.FloatField()
    OutputFrequency = models.FloatField()
    OutputActivePower = models.FloatField()
    OutputApparentPower = models.FloatField()
    BatteryAverageVoltage = models.FloatField()
    BatteryAverageCurrent = models.FloatField()
    BatteryAveragePower = models.FloatField()
    PVAverageVoltage = models.FloatField()
    PVAverageCurrent = models.FloatField()
    PVAveragePower = models.FloatField()
    PVChargingAveragePower = models.FloatField()
    LoadPercentage = models.FloatField()
    DCDCTemperature = models.FloatField()
    InverterTemperature = models.FloatField()
    BatteryStateOfCharge = models.FloatField()
    BatteryAverageCurrentFlow = models.FloatField()
    InverterChargingAverageCurrent = models.FloatField()
    PVChargingAverageCurrent = models.FloatField()
    AverageInverterEnergy = models.FloatField()
    AverageMainsEnergy = models.FloatField()
    BatteryAverageEnergy = models.FloatField()
    InverterChargingEnergy = models.FloatField()
    OutputActiveEnergy = models.FloatField()
    OutputApparentEnergy = models.FloatField()
    PVAverageEnergy = models.FloatField()
    PVChargingAverageEnergy = models.FloatField()
    AverageInverterEnergyTotal = models.FloatField()
    AverageMainsEnergyTotal = models.FloatField()
    BatteryAverageEnergyTotal = models.FloatField()
    InverterChargingEnergyTotal = models.FloatField()
    OutputActiveEnergyTotal = models.FloatField()
    OutputApparentEnergyTotal = models.FloatField()
    PVAverageEnergyTotal = models.FloatField()
    PVChargingAverageEnergyTotal = models.FloatField()
    EnergyFromFullCharge = models.FloatField()
    pass