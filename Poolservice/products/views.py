from django.shortcuts import render
from products.models import Products

# Create your views here.

def list_products (request):
    products = Products.objects.all()
    context = {
        'productos' : products
    }
    return render (request, 'products/products.html', context=context)