from django.urls import path 

from orders.views import create_order

urlpatterns = [
    path('create-order/', create_order, name='create_order'),
]