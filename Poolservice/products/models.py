from django.db import models

# Create your models here.

class Products(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=85)
    tc = models.BooleanField(default=False)
    price = models.FloatField()
    stock = models.BooleanField(default=True)

    def _str_(self):
        return self.name