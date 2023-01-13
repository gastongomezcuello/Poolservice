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

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(**form.cleaned_data)
            context = {
                'message': 'Pedido creado correctamente'
            }
            return render(request, 'orders/create-order.html', context=context)
        
        else:
            context = {
                'form_errors': form.errors,
                'form': OrderForm()
            }
            return render(request, 'orders/create-order.html', context=context)