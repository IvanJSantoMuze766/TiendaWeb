from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class SearchProductForm(forms.Form):
    busqueda = forms.CharField(max_length=100, label='Buscar Producto')

class AddToCartForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, label='Cantidad')

class ProductSearchForm(forms.Form):
    nombre = forms.CharField(max_length=100)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Aplicar cualquier validación adicional aquí
        return nombre
