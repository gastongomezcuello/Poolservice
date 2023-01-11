from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=7 , verbose_name='Código')
    description = models.CharField(max_length=85 , verbose_name='Descripción')
    tc2 = models.CharField(max_length=4 , verbose_name='TC2')
    price = models.FloatField(verbose_name='Precio')
    stock = models.BooleanField(default=False)

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'