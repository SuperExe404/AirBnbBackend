from django.urls import path
 from . import api
 
 urlpatterns = [
     path('<int:property_id>/', api.properties_detail, name='properties_detail'),
     # otras rutas...
 ]