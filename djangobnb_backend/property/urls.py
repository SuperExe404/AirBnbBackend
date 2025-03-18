from django.urls import path
from . import api
 
urlpatterns = [
    path('', api.properties_list, name='properties_list'),  # Ruta para obtener todas las propiedades
    path('create/', api.create_property, name='api_create_property'),
    path('<uuid:pk>/', api.properties_detail, name='api_properties_detail'),
    path('<uuid:pk>/book/', api.book_property, name='api_book_property'),
    path('<uuid:pk>/reservations/', api.property_reservations, name='api_property_reservations'),
]