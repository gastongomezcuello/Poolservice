from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm

# Create your views here.

def stock_check (request):
    if request.method == 'GET':
        context ={
            'form' : ProductForm()
        }
        return render(request, 'products/stock.html', context)
    # elif request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
            
def list_products (request):
    products = Products.objects.all()
    context = {
        'productos' : products
    }
    return render (request, 'products/products.html', context=context)