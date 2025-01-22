from django.urls import re_path

from main import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/display_data/$", consumers.DisplayConsumer.as_asgi()),
    
]