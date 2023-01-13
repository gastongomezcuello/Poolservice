from django.shortcuts import render
from orders.models import Order
from orders.forms import OrderForm

# Create your views here.

def create_order(request):
    if request.method == 'GET':
        context = {
            'form': OrderForm()
        }       
        return render(request, 'orders/create-order.html', context=context)
