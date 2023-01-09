from django.db import models

# Create your models here.

class Products(models.Model):
    Code = models.CharField(max_length=7)
    Description = models.CharField(max_length=85)
    TC2 = models.CharField(max_length=3)
    Price = models.FloatField()
    

    def _str_(self):
        return self.name