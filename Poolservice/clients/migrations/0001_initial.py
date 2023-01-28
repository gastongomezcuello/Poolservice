# Generated by Django 4.1.5 on 2023-01-28 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('dni', models.CharField(blank=True, max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{8}$', 'DNI inválido.')], verbose_name='DNI')),
                ('cuit', models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{11}$', 'CUIT inválido.')], verbose_name='CUIT')),
                ('kind', models.CharField(choices=[('Revendedor', 'Revendedor'), ('Cliente', 'Cliente')], max_length=20, verbose_name='Tipo')),
                ('condition', models.CharField(blank=True, choices=[('Consumidor final', 'Consumidor final'), ('Responsable inscripto', 'Responsable inscripto'), ('Iva exento', 'Iva exento')], max_length=50, verbose_name='Condición')),
                ('email', models.EmailField(max_length=40, verbose_name='Correo')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('address', models.CharField(max_length=40, verbose_name='Dirección')),
                ('city', models.CharField(max_length=40, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
