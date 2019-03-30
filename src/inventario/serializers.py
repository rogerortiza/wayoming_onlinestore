from rest_framework import serializers
from .models import Productos
from catalogos.models import CategoriasProductos
from productos.models import DetalleProducto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasProductos
        fields = ('id', 'portada', 'nombre')


class ProductosSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    foto = serializers.CharField(source='foto.url')
    colores = serializers.SerializerMethodField()
    numeros = serializers.SerializerMethodField()

    class Meta:
        model = Productos
        fields = ('id', 'categoria', 'descripcion', 'estilo', 'foto', 'no_control', 'nombre', 'precio', 'publico', 'colores', 'numeros',)

    def get_colores(self, obj):
        colores = list(obj.detalleproducto_set.all().values_list('color', flat=True).distinct())
        return colores

    def get_numeros(self, obj):
        numeros = list(obj.detalleproducto_set.all().values_list('size', flat=True).distinct())
        return numeros
