from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/detection/", consumers.DetectionConsumer.as_asgi()),
]
