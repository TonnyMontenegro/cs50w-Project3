from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields.related import RelatedField
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    # Define las posibles categorias
    Pizza = "Pizza"
    Topping = "Topping"
    Sub = "Sub"
    Pasta = "Pasta"
    Salad = "Salad"
    Cena = "Cena"
    Extra = "Extra"
    uid= models.AutoField(primary_key=True)
    Choices = (
        (Pizza,"Pizza"),
        (Topping,"Topping"),
        (Sub,"Sub"),
        (Pasta,"Pasta"),
        (Salad,"Salad"),
        (Cena,"Cena"),
        (Extra,"Extra")
    )
    nombre = models.CharField(max_length=32,choices=Choices)

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural ="Categorias"

    def __str__(self):
        return f"#{self.uid} {self.nombre}"

class Elemento(models.Model):
    # define la clase elemento que tienen en comun todos los elementos del menu
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=128,blank=False)
    uid= models.AutoField(primary_key=True)
    precio = models.DecimalField(default=1,blank=True,decimal_places=2,max_digits=6)
    P = "Pequenio"
    G = "Grande"
    NA = "Tamanio_unico"
    Choices = (
        (P,"Pequenio"),
        (G,"Grande"),
        (NA,"Tamanio_unico")
    )
    tamanio=models.CharField(max_length=50,blank=False,choices=Choices)

    def __str__(self):
        return f"{self.nombre}({self.categoria}): ${self.precio}"
    def __valido__(self):
        return (self.precio > 0)

class sub(Elemento):
    # elemento Sub del menu
    class Meta:
        verbose_name= "Sub"
        verbose_name_plural ="Subs"

    def __str__(self):
        return f"#{self.uid} {self.nombre}: {self.tamanio} - {self.precio}"

class Pasta(Elemento):
    # elemento Pasta del menu
    class Meta:
        verbose_name= "Pasta"
        verbose_name_plural ="Pastas"
    def __str__(self):
        return f"#{self.uid} {self.nombre}: {self.precio}"
    
class Ensalda(Elemento):
    # elemento Salad del menu
    class Meta:
        verbose_name= "Ensalada"
        verbose_name_plural ="Ensaladas"
    def __str__(self):
        return f"#{self.uid} {self.nombre}: {self.precio}"

class Topping(Elemento):
    # elemento Topping del menu
    class Meta:
        verbose_name= "Topping"
        verbose_name_plural ="Toppings"
    def __str__(self):
        return f"#{self.uid} {self.nombre}"

class Extra(Elemento):
    # elemento Extra del menu
    class Meta:
        verbose_name= "Extra"
        verbose_name_plural ="Extras"
    def __str__(self):
        return f"#{self.uid} {self.nombre}"

class Pizza(Elemento):
    # elemento Pizza del menu
    toppingN = models.IntegerField(default=0,blank=False)
    Regular = "Regular"
    Sicilian = "Sicilian"
    Choices=(
        (Regular,"Regular"),
        (Sicilian,"Sicilian")
    )
    tipo=models.CharField(max_length=50,blank=False,choices=Choices)

    class Meta:
        verbose_name= "Pizza"
        verbose_name_plural ="Pizzas"

    def __str__(self):
        return f"#{self.uid} Pizza {self.tipo} de {self.nombre} ({self.tamanio}): ${self.precio}"

class Cena(Elemento):
    # Elemento Dinner del menu
    class Meta:
        verbose_name= "Cena"
        verbose_name_plural ="Cena"

    def __str__(self):
        return f"#{self.uid} {self.nombre}: {self.tamanio} - {self.precio}"

class CarritoItem(models.Model):
    # Carrito del usuario
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,)
    elemento = models.ForeignKey(Elemento,on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping,blank=True,related_name="toppings_carrito")
    extra_name = models.ManyToManyField(Extra,blank=True,related_name="extra_carrito")
    cantidad = models.IntegerField(default=1)
    uid_item_cart= models.AutoField(primary_key=True)
    precio = models.DecimalField(default=1,decimal_places=2,max_digits=6)
    def __str__(self):
        return f"#{self.uid_item_cart} {self.usuario}({self.elemento} {self.cantidad}): ${self.precio}"
    def __valido__(self):
        return (self.precio > 0) 

class orden(models.Model):
    id_orden= models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,)
    fecha = models.DateTimeField(auto_now_add=True)
    monto= models.DecimalField(default=1,blank=True,decimal_places=2,max_digits=16)
    items=models.ManyToManyField(CarritoItem,related_name="items_orden")
    En_proceso = "En proceso"
    Enviada = "Enviada"
    Recibida = "Recibida"
    Carrito="Carrito"
    Orden="Orden"
    Choices_state=(
        (Carrito,"Carrito"),
        (En_proceso,"En proceso"),
        (Enviada,"Enviada"),
        (Recibida,"Recibida"),
        (Orden,"Orden")
    )
    estado = models.CharField(default=Carrito, max_length=20,choices=Choices_state)

    def __str__(self):
        return f"#{self.id_orden} {self.fecha} {self.usuario}: ${self.monto} ({self.estado})"
    def __valido__(self):
        return (self.monto > 0)

    
class Cuenta_func(models.Model):
    cuenta_numero = models.IntegerField()
    def __str__(self):
        return f"Orden #{self.cuenta_numero} "
    

