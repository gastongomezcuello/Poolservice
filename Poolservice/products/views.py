from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from products.models import Product
from products.forms import ProductForm, UpdateProductForm
from django.db import models
from django.db.models import Q
# import pandas as pd
from decimal import Decimal #, getcontext




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
    products = Product.objects.all()
    def get_price(products):

        list_prices = list()
        TC1 = 9.83
        TC2 = 10.22
        Makkintal = 200
        Moldear = 210
        if len(products) > 0:
            for product in products:
            
                if product.tc == 'Vulcano tc1':
                    list_prices.append(round((product.price * Decimal(29.9 * TC1)), 2)) 
                elif product.tc == 'Vulcano tc2':
                    list_prices.append(round((product.price * Decimal(29.9 * TC2)), 2))
                elif product.tc == 'Makkintal':
                    list_prices.append(round((product.price * Decimal(Makkintal)), 2))
                elif product.tc == 'Moldear':
                    list_prices.append(round((product.price * Decimal(Moldear)), 2))
                #the following two lines are just for order
                elif product.tc == 'LCI':
                    list_prices.append(round((product.price), 2))
                else :
                    list_prices.append(round((product.price), 2))
        return list_prices
        list_prices = get_price(products)

        context = {
            'products' : products ,
            'prices' : list_prices,
        }
        return render(request, 'products/products.html', context=context)

    queryset = request.GET.get('search')
    if queryset:
        products = Product.objects.filter(
            
            Q(code__icontains = queryset) |
            Q(description__icontains = queryset)
            ).distinct()

    if len(products) > 0:
        list_prices = get_price(products)
        context = {
            'products' : products ,
            'prices' : list_prices,
        }
    else:
        context = {
            'message_products' : 'No se encontraron resultados'
        }
    return render (request, 'products/products.html', context=context)

    