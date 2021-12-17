from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Importar .CSV
class CategoriasResource(resources.ModelResource):
    class Meta:
        model = Categoria
        exclude = ('elemento_ptr',)
        import_id_fields = ("nombre",)
class CategoriasAdmin(ImportExportModelAdmin):
    list_display=("uid", "nombre",)
    search_choices=("nombre",)
    search_fields=("nombre",)
    list_filter=("nombre",)
    resource_class = CategoriasResource

class ElementosAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio")
    search_choices=("categoria","precio","tamanio","uid")
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")


#   Pizzas
class PizzasResource(resources.ModelResource):
    class Meta:
        model = Pizza
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio","toppingN","tipo")
        # export_fields=("categoria","nombre","precio","tamanio","toppingN","tipo")
class PizzasAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio","toppingN","tipo",)
    search_choices=("categoria","precio","tamanio","uid","toppingN","tipo",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio","toppingN","tipo")

    resource_class = PizzasResource

#   Ensaladas
class EnsaldasResource(resources.ModelResource):
    class Meta:
        model = Ensalda
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio")
class EnsaldasAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio",)
    search_choices=("categoria","precio","tamanio","uid",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")
    resource_class = EnsaldasResource

#   Subs
class SubsResource(resources.ModelResource):
    class Meta:
        model = sub
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio")
class SubsAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio",)
    search_choices=("categoria","precio","tamanio","uid",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")
    resource_class = SubsResource

#   Pastas
class PastasResource(resources.ModelResource):
    class Meta:
        model = Pasta
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio")
class PastasAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio",)
    search_choices=("categoria","precio","tamanio","uid",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")
    resource_class = PastasResource

#   Toppings
class ToppingsResource(resources.ModelResource):
    class Meta:
        model = Topping
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio")
class ToppingsAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio",)
    search_choices=("categoria","precio","tamanio","uid",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")
    resource_class = ToppingsResource

#   Extras
class ExtrasResource(resources.ModelResource):
    class Meta:
        model = Extra
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio")
class ExtrasAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio",)
    search_choices=("categoria","precio","tamanio","uid",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")
    resource_class = ExtrasResource

#   Cenas
class CenasResource(resources.ModelResource):
    class Meta:
        model = Cena
        exclude = ('elemento_ptr',)
        import_id_fields = ("categoria","nombre","precio","tamanio")
class CenasAdmin(ImportExportModelAdmin):
    list_display=("uid", "categoria","nombre","precio","tamanio",)
    search_choices=("categoria","precio","tamanio","uid",)
    search_fields=("uid", "nombre","precio")
    list_filter=("categoria","tamanio")
    resource_class = CenasResource



# Register your models here.


admin.site.register(Categoria,CategoriasAdmin)
admin.site.register(Elemento,ElementosAdmin)
admin.site.register(sub,SubsAdmin)
admin.site.register(Pasta,PastasAdmin)
admin.site.register(Ensalda,EnsaldasAdmin)
admin.site.register(Topping,ToppingsAdmin)
admin.site.register(Extra,ExtrasAdmin)
admin.site.register(Cena,CenasAdmin)
admin.site.register(orden)
admin.site.register(Pizza,PizzasAdmin)
admin.site.register(CarritoItem)