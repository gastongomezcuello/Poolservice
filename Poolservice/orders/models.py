from django.db import models
from clients.models import Client
# Create your models here.

class Order(models.Model):
    
    CLIENT_CHOICES = (

    )

    PAYMENT_CHOICES = (
        ('Efectivo', 'Efectivo'), 
        ('Debito', 'Débito'),  
        ('Crédito', 'Crédito'), 
        ('Cheque', 'Cheque'), 
        ('Transferencia', 'Transferencia'), 
    )
    
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    product = models.CharField(max_length=100 , verbose_name='Producto') 
    quantity = models.FloatField(verbose_name='Cantidad')
    order_date = models.DateField(verbose_name='Fecha de pedido')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES , verbose_name='Forma de pago')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    