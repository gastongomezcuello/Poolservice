# Generated by Django 4.1.5 on 2023-01-26 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Código'),
        ),
    ]
