from django import forms
from clients.models import Client
from products.models import Product
from orders.models import Order

# class OrderForm(forms.Form):
     
#     PAYMENT_CHOICES = (
#         ('Efectivo', 'Efectivo'), 
#         ('Debito', 'Débito'),  
#         ('Crédito', 'Crédito'), 
#         ('Cheque', 'Cheque'), 
#         ('Transferencia', 'Transferencia'), 
#     )
    
#     client = forms.ModelChoiceField(queryset=Client.objects.all())
#     product = forms.ModelChoiceField(queryset=Product.objects.all())
#     quantity = forms.FloatField()
#     order_date = forms.DateField()
#     payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'quantity', 'order_date', 'payment_method']
