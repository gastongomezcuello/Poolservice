from django.urls import path

from clients.views import create_client

urlpatterns = [
    path('create-client', create_client, name='create_client'),
]