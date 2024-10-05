import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "SolarMonitor.settings"
)
django.setup()


if __name__ == '__main__':
    myCmd = 'python3 manage.py makemigrations main'
    os.system(myCmd)
    myCmd = 'python3 manage.py migrate main --run-syncdb '
    os.system(myCmd)
    from main.models import Sensor,SensorValue
    temp1_sensor = Sensor.objects.get_or_create(name = "Temperature sensor 1",ip_location = "192.168.0.6",unit="C")
    temp1_sensor = temp1_sensor[0]
    print(temp1_sensor)
    #temp1_sensor = Sensor(name = "Temperature sensor 1",ip_location = "192.168.0.6",unit="C")
    temp1_value = SensorValue(sensor = temp1_sensor,value = 43)
    temp1_sensor.save()
    temp1_value.save()
    print(list(map(lambda x :x.getDict(),Sensor.objects.all())))
    print(list(map(lambda x :x.getDict(),SensorValue.objects.all())))