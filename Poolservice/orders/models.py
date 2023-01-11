from django.db import models

# Create your models here.

class Order(models.Model):
    CHOICES = (
        ('cash', 'cash'), 
        ('debit', 'debit'), 
        ('credit', 'credit'), 
        ('check', 'check'), 
        ('crasnfer', 'crasnfer'), 
    )
    
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField()
    payment_method = models.CharField(max_length=10, choices=CHOICES)
    
    