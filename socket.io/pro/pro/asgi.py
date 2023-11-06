"""
ASGI config for pro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os
# from django.urls import path
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# import socketio
# from app import server1
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro.settings')
#
# # Create a Socket.IO server
# sio = socketio.Server()
#
# # URLRouter for WebSocket routing
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter([path('ws/my_path/',server1.YourWebSocketConsumer.as_asgi())]),  # Add WebSocket URL routing here
# })
#
# # Add the Socket.IO application to the ASGI application
# application = socketio.ASGIApp(sio, application)
#
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro.settings')

application = get_asgi_application()

