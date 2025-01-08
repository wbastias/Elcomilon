from django.contrib import admin
from . import models
from .forms import ProductForm

# Register your models here.

# en este admin.py se agrega todo lo que va a llevar el admin de la pagina que es la parte de atras de la pagina


class ProductoAdmin(admin.ModelAdmin):
    # se pasa el ProductoAdmin dentro de registo*/

    # listado en admin todos los campos
    list_display = ["nombre", "precio", "nuevo", "tipo"]

    # puede una columna sea editable*/
    list_editable = ["precio", ]

    # barra de busqueda*/
    search_fields = ["nombre"]

    # se puede filtrar por la marca o si es nuevo o no, por marca
    list_filter = ['nuevo', 'tipo']

    # se puede dividir las paginas de admin para los productos
    list_per_page = 2

    form = ProductForm

class BoletaProductInline(admin.TabularInline):
    model = models.BoletaProduct  
    extra = 1

class BoletaAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "fecha", "total"]
    search_fields = ["usuario__username", "id"]
    list_filter = ["fecha"]
    inlines = [BoletaProductInline]

admin.site.register(models.Tipo)
# productoadmin es la clases para agregar los listados de el admin
admin.site.register(models.Product, ProductoAdmin)

admin.site.register(models.Contacto)

admin.site.register(models.Boleta, BoletaAdmin)
admin.site.register(models.BoletaProduct)