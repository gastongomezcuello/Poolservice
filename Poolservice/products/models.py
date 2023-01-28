from django.db import models

# Create your models here.

class Product(models.Model):

    change_types = [
        ('Vulcano tc1','Vulcano tc1'),
        ('Vulcano tc2','Vulcano tc2'),
        ('Makkintal','Makkintal'),
        ('Moldear','Moldear'),
        ('LCI','LCI'),
        ('Ecopools','Ecopools')
        
    ]

    code = models.CharField(unique=True, max_length=15 , verbose_name='Código', blank=True, null=True)
    description = models.CharField(max_length=85 , verbose_name='Descripción')
    tc = models.CharField(max_length=20 , verbose_name='Tipo de cambio' , choices=change_types, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'