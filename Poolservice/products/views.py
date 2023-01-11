from django.shortcuts import render
from products.models import Products

# Create your views here.

def stock_check (request):
    if request.method == 'GET':
        context ={
            'form' : ProductForm()
        }
        return render(request, 'products/stock_check.html', context)
    # elif request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
            
def list_products (request):
    products = Products.objects.all()
    context = {
        'productos' : products
    }
    return render (request, 'products/products.html', context=context)