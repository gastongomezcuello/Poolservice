from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=100 , verbose_name='Nombre') 
    last_name = models.CharField(max_length=100 , verbose_name='Apellido')
    email = models.EmailField(max_length=100 , verbose_name='Correo Electrónico')
    phone = models.CharField(max_length=100 , verbose_name='Número de teléfono')
    attached_file = models.FileField(upload_to='files/', verbose_name='Archivo adjunto')
    query = models.TextField(verbose_name='¿En qué podemos ayudarte?', max_length=500)
    
	
