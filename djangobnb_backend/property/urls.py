# property/urls.py
from django.urls import path
from . import api

urlpatterns = [  # Asegúrate de que sea 'urlpatterns' y no 'urlpattern'
    path('properties/', api.properties_list, name='api_properties_list'),  # Aquí defines 'properties/'
]
