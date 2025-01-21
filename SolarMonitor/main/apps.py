from django.apps import AppConfig
from datetime import datetime, timedelta

class MainConfig(AppConfig):
    name = 'main'
    def ready(self):
        from main.tasks import poll_data
        print("start repeat")
        poll_data()