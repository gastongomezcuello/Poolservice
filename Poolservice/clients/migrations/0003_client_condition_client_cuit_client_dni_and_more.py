# Generated by Django 4.1.5 on 2023-01-22 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_client_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='condition',
            field=models.CharField(blank=True, choices=[('Consumidor final', 'Consumidor final'), ('Revendedor', 'Revendedor'), ('Responsable inscripto', 'Responsable inscripto'), ('Iva exento', 'Iva exento')], max_length=50, verbose_name='Condición'),
        ),
        migrations.AddField(
            model_name='client',
            name='cuit',
            field=models.CharField(blank=True, max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{11}$', 'CUIT inválido.')], verbose_name='CUIT'),
        ),
        migrations.AddField(
            model_name='client',
            name='dni',
            field=models.CharField(blank=True, max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{8}$', 'DNI inválido.')], verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='client',
            name='kind',
            field=models.CharField(choices=[('Revendedor', 'Revendedor'), ('Cliente', 'Cliente')], max_length=20, verbose_name='Tipo'),
        ),
    ]