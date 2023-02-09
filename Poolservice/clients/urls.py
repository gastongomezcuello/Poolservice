from django.urls import path

from clients.views import update_client , list_clients , create_client

urlpatterns = [
    path('list-clients/', list_clients, name='list_clients'),
    path('create-client/<str:username>', create_client, name='create_client'),
    path('complete-profile/', update_client, name='update_client'),
]