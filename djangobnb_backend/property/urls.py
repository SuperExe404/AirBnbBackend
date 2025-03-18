from django.urls import path
 from . import api
 
 urlpatterns = [
     path('', api.properties_list, name='properties_list'),  # Ruta para obtener todas las propiedades
     path('<uuid:property_id>/', api.properties_detail, name='properties_detail'),  # Ruta para obtener los detalles de una propiedad específica
 ]