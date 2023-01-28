from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductForm, UpdateProductForm
from django.db.models import Q


# Create your views here.

def create_product (request):
    if request.method == 'GET':
        context ={
            'form' : ProductForm()
        }
        
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            context = {
                'message': 'Producto agregado correctamente'
            }
            
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
            'form' : UpdateProductForm(
                initial={
                    'stock': product.stock,
                    'price': product.price,
            })
        }
        return render(request, 'products/update-product.html', context=context)
    elif request.method == 'POST':
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            product.price = form.cleaned_data['price']
            product.stock = form.cleaned_data['stock']
            product.save()
                
            context = {
                'message': 'Producto actualizado correctamente'
            }
            return render(request, 'products/update-product.html', context=context)
           
            
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/update-product.html', context=context)

def list_products (request):
    products = Product.objects.all()
    TC1 = 9.83
    TC2 = 10.22
    Makkintal = 200
    Moldear = 210

    for product in products:
        if products.values('tc') == 'Vulcano tc1':
            products.price = products_all.price * 29.9 * TC1 
        elif products.values('tc') == 'Vulcano tc2':
            products.price = products_all.price * 29.9 * TC2
        elif products.values('tc') == 'Makkintal':
            products.price = products_all.price * 200 * Makkintal
        elif products.values('tc') == 'Moldear':
            products.price = products_all.price * Moldear
            #the following two lines are just for order
        elif products.values('tc') == 'LCI':
            products.price = products.values('price') 
        else :
            products.price = products.values('price')

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

    