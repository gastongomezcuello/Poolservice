from django.urls import path

from clients.views import create_client , list_clients

urlpatterns = [
    path('list-clients/', list_clients, name='list_clients'),
    path('create-client/', create_client, name='create_client'),
]