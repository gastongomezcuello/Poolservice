from django.urls import path

from products.views import list_products

urlpatterns = [
    path('list-products/', list_products, name='list_products'),
]
