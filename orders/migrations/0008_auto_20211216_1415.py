# Generated by Django 3.2.9 on 2021-12-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_carritoitem_tipo_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='carritoitem',
            name='tipo_pizza',
            field=models.CharField(default='Carrito', max_length=20),
        ),
    ]
