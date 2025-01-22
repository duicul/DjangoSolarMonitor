from background_task import background
from datetime import datetime, timedelta
import logging
from main.models import Inverter, PowlandValue
logger = logging.getLogger("django")
from django.contrib.auth.models import User
from background_task.models import Task
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
@background(schedule=90)
def poll_data():
    logger.info(Task.objects.filter(task_name="main.tasks.poll_data"))
    if len(Task.objects.filter(task_name="main.tasks.poll_data")) > 1:
        return True
    #print("poll run "+str(datetime.now()))
    user = User.objects.get(username="admin")
    logger.info("PowlandPoller poll run "+str(datetime.now()) + str(user))
    
    #poll_data()
    
@background(schedule=90)
def poll_inverter(inv_id):
    try:
        print("poll_inverter run "+str(datetime.now()))
        logger.info("poll_inverter poll run"+str(datetime.now()))
        inv = Inverter.objects.get(id=inv_id)
        logger.info("poll_inverter poll inv ")
        inv_val = PowlandValue(inverter = inv, duration = 1, OperationMode = 2,EffectiveMainsVoltage = 3, MainsFrequency = 4, AverageMainsPower = 5,
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
        import channels.layers
        from asgiref.sync import async_to_sync
        channel_layer = channels.layers.get_channel_layer()
        data = serializers.serialize("json", [inv_val], cls=DjangoJSONEncoder)
        logger.info("poll_inverter poll inv "+str(data))
        async_to_sync(channel_layer.group_send)('data_display', {"type": "data.message", "message": data})
    except Exception as e:
        logger.error("poll_inverter poll Exception "+str(e))
        print(e)