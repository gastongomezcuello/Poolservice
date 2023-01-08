from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=40)
    kind = models.CharField(max_length=20)
    