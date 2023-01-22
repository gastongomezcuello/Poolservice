from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm
from django.db.models import Q


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

def update_product (request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        context ={
            'form' : ProductForm(
                initial={
                    'stock': product.stock,
                    'price': product.price,
            })
        }
        return render(request, 'products/update-product.html', context=context)
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.update(**form.cleaned_data)
            context = {
                'message': 'Producto actualizado correctamente'
            }
            return render(request, 'products/update-product.html', context=context)
           
            
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create-product.html', context=context)

def list_products (request):
    products = Product.objects.all()
    queryset = request.GET.get('search')
    if queryset:
        products = Product.objects.filter(
            
            Q(code__icontains = queryset) |
            Q(description__icontains = queryset)
            ).distinct()

    if len(products) > 0:    
        context = {
            'products' : products ,
        }
    else:
        context = {
            'message_products' : 'No se encontraron resultados'
        }
    return render (request, 'products/products.html', context=context)