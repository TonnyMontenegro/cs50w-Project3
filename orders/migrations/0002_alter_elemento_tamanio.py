# Generated by Django 3.2.9 on 2021-12-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='tamanio',
            field=models.CharField(choices=[('Pequenio', 'Pequenio'), ('Grande', 'Grande'), ('Tamanio_unico', 'Tamanio_unico')], max_length=50),
        ),
    ]