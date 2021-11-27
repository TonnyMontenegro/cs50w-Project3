# Generated by Django 3.2.9 on 2021-11-24 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Pizza', 'Pizza'), ('Topping', 'Topping'), ('Sub', 'Sub'), ('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Cena', 'Cena')], max_length=14)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cuenta_func',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta_numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('precio', models.IntegerField(blank=True, default=1)),
                ('tamanio', models.CharField(blank=True, choices=[(' Pequeño', 'Pequeño'), ('Grande', 'Grande')], max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cena',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
            ],
            options={
                'verbose_name': 'Cena',
                'verbose_name_plural': 'Cena',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='Ensalda',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
            ],
            options={
                'verbose_name': 'Ensalada',
                'verbose_name_plural': 'Ensaladas',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
            ],
            options={
                'verbose_name': 'Extra',
                'verbose_name_plural': 'Extras',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
            ],
            options={
                'verbose_name': 'Pasta',
                'verbose_name_plural': 'Pastas',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
                ('toppingN', models.IntegerField(default=0)),
                ('tipo', models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Sicilian', 'Sicilian')], max_length=50)),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizzas',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='sub',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
            ],
            options={
                'verbose_name': 'Sub',
                'verbose_name_plural': 'Subs',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('elemento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.elemento')),
            ],
            options={
                'verbose_name': 'Topping',
                'verbose_name_plural': 'Toppings',
            },
            bases=('orders.elemento',),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y hora: ')),
                ('direccion', models.CharField(blank=True, max_length=150)),
                ('comentario', models.CharField(blank=True, max_length=150)),
                ('total', models.IntegerField(default=0, verbose_name='Total')),
                ('numero', models.IntegerField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Recibido', 'Recibido')], default='Pendiente', max_length=20)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.elemento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.BooleanField(default='false')),
                ('cantidad', models.IntegerField(default=1)),
                ('precio', models.IntegerField(default=1)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.elemento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topping', models.ManyToManyField(blank=True, related_name='ordenes', to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.BooleanField(default='false')),
                ('cantidad', models.IntegerField(default=1)),
                ('precio', models.IntegerField(default=1)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.elemento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemcarrito', to=settings.AUTH_USER_MODEL)),
                ('topping', models.ManyToManyField(blank=True, related_name='Itemscarrito', to='orders.Topping')),
            ],
        ),
    ]
