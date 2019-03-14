from rest_framework import viewsets
from .models import Productos
from .serializers import ProductosSerializer


class ProductosViewset(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer