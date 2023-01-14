# Generated by Django 4.1.5 on 2023-01-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tc2',
        ),
        migrations.AddField(
            model_name='product',
            name='tc',
            field=models.CharField(choices=[('Vulcano tc1', 'Vulcano tc1'), ('Vulcano tc2', 'Vulcano tc2'), ('Makkintal', 'Makkintal'), ('Moldear', 'Moldear')], default='NULL', max_length=20, verbose_name='Tipo de cambio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=10, unique=True, verbose_name='Código'),
        ),
    ]
