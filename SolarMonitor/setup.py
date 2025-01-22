import os
import django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "SolarMonitor.settings"
)
django.setup()
from main.models import Inverter, PowlandValue
from django.contrib.auth.models import User
if __name__ == '__main__':
    myCmd = 'python manage.py makemigrations'
    os.system(myCmd)
    myCmd = 'python manage.py migrate '
    os.system(myCmd)
    user = User.objects.get(username="admin")
    if not user: 
        user = User.objects.create_user(username='admin',password='admin')
    inv = Inverter.objects.get(id=3)
    inv_val = PowlandValue(inverter = inv,duration = 1, OperationMode = 2,EffectiveMainsVoltage = 3, MainsFrequency = 4, AverageMainsPower = 5,
                           EffectiveInverterVoltage = 6, EffectiveInverterCurrent = 7, InverterFrequency = 8, AverageInverterPower = 9,
                           InverterChargingPower = 10,OutputEffectiveVoltage = 11, OutputEffectiveCurrent = 12, OutputFrequency = 13, OutputActivePower = 14,
                           OutputApparentPower = 15, BatteryAverageVoltage = 16,BatteryAverageCurrent = 17, BatteryAveragePower = 18, PVAverageVoltage = 19,
                           PVAverageCurrent = 20,PVAveragePower = 20, PVChargingAveragePower = 20,LoadPercentage = 20,DCDCTemperature = 20,InverterTemperature = 20,
                           BatteryStateOfCharge = 20,BatteryAverageCurrentFlow = 20,InverterChargingAverageCurrent = 20,PVChargingAverageCurrent = 20,
                           AverageInverterEnergy = 20,AverageMainsEnergy = 20,BatteryAverageEnergy = 20,InverterChargingEnergy = 20,OutputActiveEnergy = 20,
                           OutputApparentEnergy = 20,PVAverageEnergy = 20,PVChargingAverageEnergy = 20,AverageInverterEnergyTotal = 20,AverageMainsEnergyTotal = 20,
                           BatteryAverageEnergyTotal = 20,InverterChargingEnergyTotal = 20,OutputActiveEnergyTotal = 20,OutputApparentEnergyTotal = 20,
                           PVAverageEnergyTotal = 20,PVChargingAverageEnergyTotal = 20,EnergyFromFullCharge = 20)
    inv_val.save()
    #from main.models import Sensor,SensorValue
    #temp1_sensor = Sensor.objects.get_or_create(name = "Temperature sensor 1",ip_location = "192.168.0.6",unit="C")
    #temp1_sensor = temp1_sensor[0]
    #print(temp1_sensor)
    #temp1_sensor = Sensor(name = "Temperature sensor 1",ip_location = "192.168.0.6",unit="C")
    #temp1_value = SensorValue(sensor = temp1_sensor,value = 43)
    #temp1_sensor.save()
    #temp1_value.save()
    #print(list(map(lambda x :x.getDict(),Sensor.objects.all())))
    #print(list(map(lambda x :x.getDict(),SensorValue.objects.all())))