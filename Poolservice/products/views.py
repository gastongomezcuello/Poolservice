from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm


# Create your views here.

def create_product (request):
    if request.method == 'GET':
        context ={
            'form' : ProductForm()
        }
        return render(request, 'products/create-product.html', context=context)
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            context = {
                'message': 'Producto agregado correctamente'
            }
            return render(request, 'products/create-product.html', context=context)
            
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create-product.html', context=context)

def list_products (request):
    products = Product.objects.all()
    

    context = {
        'products' : products ,
       
    }
    return render (request, 'products/products.html', context=context)