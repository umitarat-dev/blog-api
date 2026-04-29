"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from drf_yasg.generators import OpenAPISchemaGenerator
from django.conf import settings

class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        # Swagger'a 'Authorization' header'ı bekleyen bir kutu ekle diyoruz
        schema.schemes = ["http", "https"] if settings.DEBUG else ["https"]
        schema.security_definitions = {
            'Token': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header'
            }
        }
        schema.security = [{"Token": []}]
        return schema


# Swagger dokümantasyon ayarları
schema_view = get_schema_view(
   openapi.Info(
      title="Blog App API",
      default_version='v1',
      description="API for blogging with nested comments and likes, and interactions",
      contact=openapi.Contact(email="umitarat8098@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   generator_class=JWTSchemaGenerator,
)
    
    
urlpatterns = [
    # Ana sayfa direkt Swagger'a gitsin
    path('', RedirectView.as_view(url='swagger/', permanent=True)),
    
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path("blog/", include("blog.urls")),
    
    # Swagger ve Redoc yolları
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
