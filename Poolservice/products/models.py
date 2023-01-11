from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=85)
    tc2 = models.CharField(max_length=4)
    price = models.FloatField()
    stock = models.BooleanField(default=False)
    
    

    def _str_(self):
        return self.name