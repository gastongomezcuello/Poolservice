from django.urls import path

from products.views import list_products , stock_check

urlpatterns = [
    path('list-products/', list_products, name='list_products'),
    path('stock-check/', stock_check, name='stock_check'),
]

