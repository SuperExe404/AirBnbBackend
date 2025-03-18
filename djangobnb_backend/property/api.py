from django.http import JsonResponse
 from rest_framework.decorators import api_view, authentication_classes, permission_classes
 from .models import Property
 from .serializers import PropertiesDetailSerializer
 
 @api_view(['GET'])
 @authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
 @permission_classes([])  # Aquí puedes agregar permisos si es necesario
 def properties_detail(request, property_id):
     try:
         property = Property.objects.get(id=property_id)  # Obtén la propiedad por ID
     except Property.DoesNotExist:
         return JsonResponse({'error': 'Property not found'}, status=404)
 
     serializer = PropertiesDetailSerializer(property)  # No se usa 'many=True' aquí
 
     return JsonResponse({
         'data': serializer.data
     })


 @api_view(['GET'])
 @authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
 @permission_classes([])  # Aquí puedes agregar permisos si es necesario
 def properties_list(request):
     properties = Property.objects.all()  # Obtener todas las propiedades
     serializer = PropertiesDetailSerializer(properties, many=True)  # Serializar múltiples propiedades
     return JsonResponse({'data': serializer.data})