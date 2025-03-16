# djangobnb_backend/urls.py o el archivo principal de URLs
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('property.urls')),  # Aquí incluyes las URLs de la app 'property'
]
