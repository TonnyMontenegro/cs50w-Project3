# Generated by Django 3.2.9 on 2021-12-05 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritoitem',
            name='cantidad',
        ),
    ]
