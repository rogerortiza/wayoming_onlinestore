from django.test import TestCase
from catalogos.models import CategoriasProductos
from inventario.models import Productos


class TestInventario(TestCase):

    def setUp(self):
        categoria = CategoriasProductos.objects.create()
        Productos.objects.create(no_control='999999', categoria=categoria, nombre='Piteado_test', descripcion='cinto_test', almacen='Centro_test',
                                 costo=300, precio=700.00)

    def test_producto(self):
        """Product must be an instance a Productos class"""
        producto = Productos.objects.get(nombre="Piteado_test")
        self.assertEqual(True, isinstance(producto, Productos))
