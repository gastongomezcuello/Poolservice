# Generated by Django 4.1.5 on 2023-01-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Código'),
        ),
    ]
