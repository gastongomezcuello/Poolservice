from django.urls import path

from clients.views import update_client , list_clients

urlpatterns = [
    path('list-clients/', list_clients, name='list_clients'),
    path('complete-profile/', update_client, name='update_client'),
]