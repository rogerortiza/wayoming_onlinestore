from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Productos


class ProductosList(ListView):
    model = Productos
    template_name = "inventario/lista_productos.html"
    context_object_name = "lista_productos"

class ProductoDetalle(DetailView):
    model = Productos
    template_name = "productos/detalle_producto.html"
    queryset = Productos.objects.all()
    context_object_name = "producto"
