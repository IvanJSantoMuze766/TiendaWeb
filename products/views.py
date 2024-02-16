from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Carrito
from .forms import ProductForm, AgregarAlCarritoForm
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics, viewsets
from .serializers import ProductSerializer


def product_list_view(request, orden=None):
    ordenamientos = {
        'alfabetico': 'title',
        'precio_asc': 'price',
        'precio_desc': '-price',
        'relevancia': '-id',  # Cambiado a '-id' para mantener un orden estable
    }
    ordenamiento = ordenamientos.get(orden, None)
    products = Product.objects.all().order_by(ordenamiento) if ordenamiento else Product.objects.all()
    return render(request, 'base.html', {'products': products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')


def product_list_by_category(request, categoria=None):
    products = Product.objects.filter(category=categoria) if categoria else Product.objects.all()
    categorias = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'product_list.html', {'products': products, 'categorias': categorias, 'categoria_actual': categoria})


def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'ver_carrito.html', {'carrito': carrito})


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)

    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            # Lógica para agregar el producto al carrito
            return redirect('carrito_compras')
    else:
        return redirect('detalle_producto', product_id=producto_id)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def politica_devoluciones(request):
    return render(request, 'politica_devoluciones.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class ListaProductosAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetalleProductoAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def buscar_producto_por_nombre(nombre):
    return Product.objects.filter(title=nombre).first()


def buscar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            producto = Product.objects.filter(title=nombre).first()
            if producto:
                # Procesar el producto encontrado
                pass
            else:
                # Manejar el caso de producto no encontrado
                pass
        else:
            # Manejar el caso de entrada de usuario vacía o inválida
            pass
    return render(request, 'buscar_producto.html')
