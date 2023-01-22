from django.db import models
from django.core import validators
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):

    KIND_CHOICES = (
        ('Revendedor', 'Revendedor'),
        ('Cliente', 'Cliente'),        
    )
    CONDITION_CHOICES = (
        ('Consumidor final', 'Consumidor final'),
        ('Responsable inscripto', 'Responsable inscripto'),
        ('Iva exento', 'Iva exento'),
    )
    
    name = models.CharField(max_length=40 , verbose_name='Nombre')
    dni = models.CharField(max_length=8, validators=[ 
        validators.RegexValidator(r'^[0-9]{8}$', 'DNI inválido.')], verbose_name='DNI' , null=True, blank=True , unique=True , ) 
    cuit = models.CharField(max_length=11 , validators=[ 
        validators.RegexValidator(r'^[0-9]{11}$', 'CUIT inválido.')], verbose_name='CUIT' , null=True, blank=True , unique=True)
    kind = models.CharField(max_length=20 , choices=KIND_CHOICES, verbose_name='Tipo')
    condition = models.CharField(max_length=50 , choices=CONDITION_CHOICES, verbose_name='Condición', blank=True)
    email = models.EmailField(max_length=40 , verbose_name='Correo')
    phone = models.CharField(max_length=20 , verbose_name='Teléfono')
    address = models.CharField(max_length=40 , verbose_name='Dirección')
    city = models.CharField(max_length=40 , verbose_name='Ciudad')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
      
