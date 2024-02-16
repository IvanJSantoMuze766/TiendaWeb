from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'seller', 'imagen']  # Selecciona los campos que deseas serializar

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name  # Serializa el nombre de la categoría en lugar del objeto Category completo
        return representation
