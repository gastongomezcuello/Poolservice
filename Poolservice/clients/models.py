from django.db import models

# Create your models here.

class Client(models.Model):

    KIND_CHOICES = (
        ('Revendedor/a', 'Revendedor/a'),
        ('Cliente', 'Cliente'),        
    )

    name = models.CharField(max_length=40 , verbose_name='Nombre')
    kind = models.CharField(max_length=20 , choices=KIND_CHOICES, verbose_name='Tipo')
    email = models.EmailField(max_length=40 , verbose_name='Correo')
    phone = models.CharField(max_length=20 , verbose_name='Teléfono')
    address = models.CharField(max_length=40 , verbose_name='Dirección')
    city = models.CharField(max_length=40 , verbose_name='Ciudad')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
      
