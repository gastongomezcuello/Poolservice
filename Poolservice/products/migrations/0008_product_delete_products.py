# Generated by Django 4.1.5 on 2023-01-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_stock_products_tc2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('description', models.CharField(max_length=85)),
                ('tc2', models.CharField(max_length=4)),
                ('price', models.FloatField()),
                ('stock', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
