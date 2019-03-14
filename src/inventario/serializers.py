from rest_framework import serializers
from .models import Productos
from catalogos.models import CategoriasProductos


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasProductos
        fields = ('id', 'portada', 'nombre')


class ProductosSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    foto = serializers.CharField(source='foto.url')

    class Meta:
        model = Productos
        fields = ('id', 'categoria', 'descripcion', 'estilo', 'foto', 'no_control', 'nombre', 'precio', 'publico',)
