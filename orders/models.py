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
    Choices = (
        (Pizza,"Pizza"),
        (Topping,"Topping"),
        (Sub,"Sub"),
        (Pasta,"Pasta"),
        (Salad,"Salad"),
        (Cena,"Cena"),
    )
    nombre = models.CharField(max_length=14,choices=Choices)

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural ="Categorias"

    def __str__(self):
        return f"{self.nombre}"

class Elemento(models.Model):
    # define la clase elemento que tienen en comun todos los elementos del menu
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=128)
    precio = models.IntegerField(default=1,blank=False)
    P = " Pequeño"
    G = "Grande"
    Choices = (
        (P,"Pequeño"),
        (G,"Grande"),
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
        return f"{self.nombre}: {self.tamanio} - {self.precio}"

class Pasta(Elemento):
    # elemento Pasta del menu
    class Meta:
        verbose_name= "Pasta"
        verbose_name_plural ="Pastas"
    def __str__(self):
        return f"{self.nombre}: {self.precio}"
    
class Ensalda(Elemento):
    # elemento Salad del menu
    class Meta:
        verbose_name= "Ensalada"
        verbose_name_plural ="Ensaladas"
    def __str__(self):
        return f"{self.nombre}: {self.precio}"

class Topping(Elemento):
    # elemento Topping del menu
    class Meta:
        verbose_name= "Topping"
        verbose_name_plural ="Toppings"
    def __str__(self):
        return f"{self.nombre}"

class Extra(Elemento):
    # elemento Extra del menu
    class Meta:
        verbose_name= "Extra"
        verbose_name_plural ="Extras"
    def __str__(self):
        return f"{self.nombre}"

class Pizza(Elemento):
    # elemento Pizza del menu
    toppingN = models.IntegerField(default=0)
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
        return f"pizza {self.nombre} ({self.tipo} {self.tamanio}): ${self.precio}"

class Cena(Elemento):
    # Elemento Dinner del menu
    class Meta:
        verbose_name= "Cena"
        verbose_name_plural ="Cena"

    def __str__(self):
        return f"{self.nombre}: {self.tamanio} - {self.precio}"


class Carrito(models.Model):
    # Carrito del usuario
    usuario = models.ForeignKey(User,related_name="itemcarrito",on_delete=models.CASCADE,)
    elemento = models.ForeignKey(Elemento,on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping,related_name="Itemscarrito",blank=True)
    extra =models.BooleanField(default="false")
    cantidad = models.IntegerField(default=1)
    precio = models.IntegerField(default=1,)

    def __str__(self):
        return f"{self.nombre}({self.categoria}): ${self.precio}"
    def __valido__(self):
        return (self.precio > 0)

class Orden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping,related_name="ordenes",blank=True)
    extra =models.BooleanField(default="false")
    cantidad = models.IntegerField(default=1)
    precio = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.nombre}({self.categoria}): ${self.precio}"
    def __valido__(self):
        return (self.precio > 0)

class Factura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="factura")
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    fecha = models.DateTimeField("Fecha y hora: ",default=timezone.now)
    direccion = models.CharField(max_length=150,blank=True)
    comentario = models.CharField(max_length=150,blank=True)
    total = models.IntegerField("Total", default=0)
    numero=models.IntegerField()
    Pendiente = "Pendiente"
    Completado = "Completada"
    Recibido = "Recibido"
    Choices=(
        (Pendiente,"Pendiente"),
        (Completado,"Completada"),
        (Recibido,"Recibido")
    )
    estado = models.CharField(default=Pendiente, max_length=20,choices=Choices)

    def __str__(self):
        return f"{self.usuario} {self.fecha}: {self.estado}"
    def __valido__(self):
        return (self.total > 0)
    
class Cuenta_func(models.Model):
    cuenta_numero = models.IntegerField()
    def __str__(self):
        return f"Orden #{self.contador} "
    

