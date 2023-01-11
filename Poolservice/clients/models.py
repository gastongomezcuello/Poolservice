from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=40)
    kind = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
