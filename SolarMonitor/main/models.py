from django.db import models

import json


# Create your models here.
class User_db(models.Model): 
   username = models.CharField(max_length = 100 , unique=True)
   password = models.CharField(max_length = 100 , unique=True)
   def getDict(self):
        return {"username":self.username,"password":self.password}