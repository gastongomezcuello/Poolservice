from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from products.models import Product
from products.forms import ProductForm, UpdateProductForm
from django.db.models import Q


# Create your views here.
@login_required()
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
@login_required()
def update_product (request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        context ={
            'form' : UpdateProductForm(
                initial={
                    'stock': product.stock,
                    'price': product['price'],
            })
        }
        return render(request, 'products/update-product.html', context=context)
    elif request.method == 'POST':
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            product['price'] = form.cleaned_data['price']
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
    products = list(Product.objects.all())
    
   
    
    TC1 = 9.83
    TC2 = 10.22
    Makkintal = 200
    Moldear = 210

    for product in products:
        if products[2] == 'Vulcano tc1':
            products[3] = products[3] * 29.9 * TC1 
        elif products[2] == 'Vulcano tc2':
            products[3] = products[3] * 29.9 * TC2
        elif products[2] == 'Makkintal':
            products[3] = products[3] * 200 * Makkintal
        elif products[2] == 'Moldear':
            products[3] = products[3] * Moldear
            #the following two lines are just for order
        elif products[2] == 'LCI':
            products[3] = products[3] 
        else :
            products[3] = products[3]

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

    