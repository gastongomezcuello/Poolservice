# Generated by Django 4.1.5 on 2023-01-10 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_products_stock_remove_products_tc2'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='TC2',
            field=models.CharField(default='tc2', max_length=4),
            preserve_default=False,
        ),
    ]
