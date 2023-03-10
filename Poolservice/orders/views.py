from django.shortcuts import render
from orders.models import Order
from orders.forms import OrderForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(**form.cleaned_data)
            context = {
                'message': 'Pedido creado correctamente'
            }
             
        else:
            context = {
                'form_errors': form.errors,
                'form': OrderForm()
            }
            
    else:
        context = {
            'form': OrderForm()
        }            
    
    return render(request, 'orders/create-order.html', context=context)
@login_required()
def list_orders (request):
    orders = Order.objects.all()
    queryset = request.GET.get('search')
    if queryset:
        orders = Order.objects.filter(

            Q(id__icontains = queryset)
        )
    if len(orders) > 0:
        context = {
            'orders': orders,
        }
    else: 
        context = {
            'message_orders': 'No hay pedidos registrados'
        }
    return render (request, 'orders/orders.html', context=context)