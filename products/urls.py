from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('product/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('product/<int:producto_id>/agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/', views.product_list, name='product_list'),
    path('products/<str:categoria>/', views.product_list, name='lista_productos_por_categoria'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('api/products/', views.ListaProductosAPI.as_view(), name='lista_productos_api'),
    path('api/product/<int:pk>/', views.DetalleProductoAPI.as_view(), name='detalle_producto_api'),
]

handler404 = 'TiendaWeb.views.error_404'
