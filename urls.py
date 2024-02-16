from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Definir la vista de esquema para la documentación API
schema_view = get_schema_view(
    openapi.Info(
        title="TiendaWeb API",
        default_version='v1',
        description="API de TiendaWeb para gestionar productos",
        terms_of_service="https://www.TiendaWeb.com/terms/",
        contact=openapi.Contact(email="contacto@TiendaWeb.com"),
        license=openapi.License(name="Licencia de TiendaWeb"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Definir las URL
urlpatterns = [
    # URL para el panel de administración de Django
    path('admin/', admin.site.urls),
    
    # URLs de la aplicación principal TiendaWeb
    path('TiendaWeb/', include('TiendaWeb.urls')),
    
    # URLs de otras aplicaciones como 'tuaplicacion'
    path('tuaplicacion/', include('tuaplicacion.urls')),
    
    # URL para la documentación de la API utilizando Swagger
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Configurar el enrutador para las vistas basadas en ViewSet
router = DefaultRouter()
router.register(r'productos', ProductViewSet, basename='producto')

