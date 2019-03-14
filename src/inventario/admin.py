""" Admin panel models register """
from django.contrib import admin
from .models import Productos
from productos.models import DetalleProducto

# Register your models here.
class DetalleProductoInline(admin.TabularInline):
    model = DetalleProducto
    can_delete = False

class ProductosAdmin(admin.ModelAdmin):
    """ Product information """

    list_display = ('id', 'no_control', 'nombre', 'descripcion', 'cantidad', 'fecha_registro')
    exclude = ('no_control',)
    inlines = [DetalleProductoInline,]

admin.site.register(Productos, ProductosAdmin)
