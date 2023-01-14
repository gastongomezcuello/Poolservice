from django.urls import path 

from orders.views import create_order , list_orders

urlpatterns = [
    path('list-orders/', list_orders, name='list_orders'),
    path('create-order/', create_order, name='create_order'),
]