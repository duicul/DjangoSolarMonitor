import os

myCmd = 'python3 manage.py makemigrations main'
os.system(myCmd)
myCmd = 'python3 manage.py migrate'
os.system(myCmd)