from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Eliminado el argumento 'max_length' ya que no es válido para ForeignKey
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)  # Corregido el nombre de 'imagen' a 'image'

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):  # Renombrado 'Carrito' a 'ShoppingCart' para seguir convenciones de nombres en inglés
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Renombrado 'usuario' a 'user' para seguir convenciones de nombres en inglés
    products = models.ManyToManyField(Product, through='CartItem')  # Corregido el nombre del modelo 'Producto' a 'Product'


class CartItem(models.Model):  # Cambiado 'ItemCarrito' a 'CartItem' para seguir convenciones de nombres en inglés
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)  # Cambiado 'carrito' a 'cart' para seguir convenciones de nombres en inglés
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Cambiado 'producto' a 'product' para seguir convenciones de nombres en inglés
    quantity = models.PositiveIntegerField(default=1)  # Renombrado 'cantidad' a 'quantity' para seguir convenciones de nombres en inglés

    def __str__(self):
        return self.product.title  # Corregido el acceso al título del producto

