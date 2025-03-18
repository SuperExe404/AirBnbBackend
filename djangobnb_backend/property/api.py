from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Property
from .serializers import PropertiesDetailSerializer
from .forms import PropertyForm

@api_view(['GET'])
@authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
@permission_classes([])  # Aquí puedes agregar permisos si es necesario
def properties_detail(request, property_id):
    try:
        property_obj = Property.objects.get(id=property_id)  # Cambio 'property' a 'property_obj' para evitar conflicto con la palabra clave
    except Property.DoesNotExist:
        return JsonResponse({'error': 'Property not found'}, status=404)

    serializer = PropertiesDetailSerializer(property_obj)  # No se usa 'many=True' aquí
    return JsonResponse({'data': serializer.data})


@api_view(['GET'])
@authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
@permission_classes([])  # Aquí puedes agregar permisos si es necesario
def properties_list(request):
    properties = Property.objects.all()  # Obtener todas las propiedades
    serializer = PropertiesDetailSerializer(properties, many=True)  # Serializar múltiples propiedades
    
    return JsonResponse({'data': serializer.data})  # Corrección de 'serializers.data' a 'serializer.data'


@api_view(['POST'])  # 'FILES' no es un método HTTP válido, se elimina.
@authentication_classes([])  
@permission_classes([])  
def create_property(request):
    form = PropertyForm(request.POST, request.FILES)

    if form.is_valid():
        property_obj = form.save(commit=False)
        property_obj.landlord = request.user
        property_obj.save()
        return JsonResponse({'success': True})
    
    return JsonResponse({'errors': form.errors.get_json_data()}, status=400)  # Mejora en el manejo de errores
