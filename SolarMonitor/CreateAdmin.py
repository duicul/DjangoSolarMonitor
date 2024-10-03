import hashlib
import os

import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "WebVideoPlayer.settings"
)
django.setup()

if __name__ == '__main__':
    from main.models import User_db
    #instance = User_db.objects.get(id="admin")
    #instance.delete()
    username="admin"
    password="admin"
    text_pass = hashlib.sha512(password.encode())
    encrypt_pass = text_pass.hexdigest()
    user_db=User_db(username=username,password=encrypt_pass)
    user_db.save()
