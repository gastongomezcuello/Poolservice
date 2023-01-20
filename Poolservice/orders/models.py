from django.db import models
from clients.models import Client
from products.models import Product
# Create your models here.

class Order(models.Model):
    

    PAYMENT_CHOICES = (
        ('Efectivo', 'Efectivo'), 
        ('Debito', 'Débito'),  
        ('Crédito', 'Crédito'), 
        ('Cheque', 'Cheque'), 
        ('Transferencia', 'Transferencia'), 
    )
    order_number = models.IntegerField(auto_created=True, null=True, blank=True, unique=True, verbose_name='Número de pedido')
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Cliente')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Producto')
    quantity = models.FloatField(verbose_name='Cantidad', default=1)
    order_date = models.DateField(verbose_name='Fecha de pedido')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES , verbose_name='Forma de pago')

    def __str__(self):
        return f'{self.client} compró {self.quantity} {self.product}'
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    