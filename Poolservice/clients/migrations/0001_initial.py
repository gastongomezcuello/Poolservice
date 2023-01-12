# Generated by Django 4.1.5 on 2023-01-12 16:27

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
                ('kind', models.CharField(choices=[('Revendedor/a', 'Revendedor/a'), ('Cliente', 'Cliente')], max_length=20, verbose_name='Tipo')),
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
