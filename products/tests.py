from django.test import TestCase
from django.urls import reverse
from .models import Product
from .views import product_list_view


class ProductListViewTestCase(TestCase):
    def setUp(self):
        # Creamos productos de ejemplo para probar la vista de lista de productos
        self.product1 = Product.objects.create(name='Producto 1', price=10)
        self.product2 = Product.objects.create(name='Producto 2', price=20)

    def test_product_list_view_status_code(self):
        """
        Verifica que la vista de lista de productos devuelve el código de estado HTTP 200 (OK).
        """
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_contains_products(self):
        """
        Verifica que la vista de lista de productos muestra los productos creados en setUp.
        """
        response = self.client.get(reverse('product_list'))
        self.assertIn(self.product1, response.context['products'])
        self.assertIn(self.product2, response.context['products'])

    def test_product_list_view_uses_correct_template(self):
        """
        Verifica que la vista de lista de productos utiliza el template correcto.
        """
        response = self.client.get(reverse('product_list'))
        self.assertTemplateUsed(response, 'product_list.html')

    def test_product_list_view_pagination(self):
        """
        Verifica que la vista de lista de productos pagine correctamente los resultados.
        """
        # Creamos más productos para alcanzar el límite de paginación
        for i in range(15):
            Product.objects.create(name=f'Producto {i+3}', price=(i+3)*10)

        response = self.client.get(reverse('product_list'))
        self.assertEqual(len(response.context['products']), 10)  # Debería mostrar 10 productos por página

    def test_product_list_view_orders_products_correctly(self):
        """
        Verifica que la vista de lista de productos muestra los productos en el orden correcto.
        """
        # Cambiamos el orden de los productos creados en setUp
        self.product1.price = 30
        self.product1.save()
        self.product2.price = 5
        self.product2.save()

        response = self.client.get(reverse('product_list'))
        products = response.context['products']
        # Producto 2 debería estar primero por ser más barato
        self.assertEqual(products[0], self.product2)
        # Producto 1 debería estar segundo por ser más caro
        self.assertEqual(products[1], self.product1)
