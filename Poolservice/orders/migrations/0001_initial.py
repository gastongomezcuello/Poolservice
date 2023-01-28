# Generated by Django 4.1.5 on 2023-01-28 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1, verbose_name='Cantidad')),
                ('order_date', models.DateField(verbose_name='Fecha de pedido')),
                ('payment_method', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Debito', 'Débito'), ('Crédito', 'Crédito'), ('Cheque', 'Cheque'), ('Transferencia', 'Transferencia')], max_length=20, verbose_name='Forma de pago')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Cliente')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
