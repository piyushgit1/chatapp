from django.urls import re_path
from mapp import consumers

websocket_urlpatterns = [
    re_path(r'ws/mapp/(?P<user_name>\w+)/(?P<room_name>\w+)/$', consumers.ChatConsumer)
]


