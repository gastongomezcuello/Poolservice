from django.db import models

# Create your models here.

class Orders(models.Model):
    CHOICES = (
        ('Cash', 'Cash'), 
        ('Debit', 'Debit'), 
        ('Credit', 'Credit'), 
        ('Check', 'Check'), 
        ('Trasnfer', 'Trasnfer'), 
    )
    
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField()
    payment_method = models.CharField(max_length=10, choices=CHOICES)
    
    