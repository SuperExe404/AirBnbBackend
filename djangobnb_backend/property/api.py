from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import PropertyForm
from .models import Property , Reservation
from .serializers import PropertiesListSerializer, PropertiesDetailSerializer, ReservationsListSerializer
from rest_framework_simplejwt.tokens import AccessToken
from useraccount.models import User
 
@api_view(['GET'])
@authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
@permission_classes([])  # Aquí puedes agregar permisos si es necesario
def properties_list(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer ')[1]
        token = AccessToken(token)
        user_id = token.payload['user_id']
        user = User.objects.get(pk=user_id)
    except Exception as e:
        user = None
 
 
    favorites = []
    properties = Property.objects.all()  # Obtener todas las propiedades
    is_favorites = request.GET.get('is_favorites', '')

    landlord_id = request.GET.get('landlord_id', '')
    if is_favorites:
         properties = properties.filter(favorited__in=[user])
 
    if user:
        for property in properties:
            if user in property.favorited.all():
                favorites.append(property.id)
 
    if landlord_id:
        properties = properties.filter(landlord_id = landlord_id)
    serializer = PropertiesListSerializer(properties, many=True)  # Serializar múltiples propiedades
 
    return JsonResponse({
        'data': serializer.data,
        'favorites': favorites    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def property_reservations(request, pk):
    property = Property.objects.get(pk=pk)
    reservations = property.reservations.all()

    serializer = ReservationsListSerializer(reservations, many=True)
 
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
@permission_classes([])  # Aquí puedes agregar permisos si es necesario
def properties_list(request):
    properties = Property.objects.all()  # Obtener todas las propiedades
    serializer = PropertiesDetailSerializer(properties, many=True)  # Serializar múltiples propiedades
    
    return JsonResponse(serializer.data)

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
    
    return JsonResponse({'errors': form.errors.get_json_data()}, status=400)

@api_view(['POST'])
def book_property(request, pk):
    try:
         start_date = request.POST.get('start_date', '')
         end_date = request.POST.get('end_date', '')
         number_of_nights = request.POST.get('number_of_nights', '')
         total_price = request.POST.get('total_price', '')
         guests = request.POST.get('guests', '')
 
         property = Property.objects.get(pk=pk)
 
         Reservation.objects.create(
             property=property,
             start_date=start_date,
             end_date=end_date,
             number_of_nights=number_of_nights,
             total_price=total_price,
             guests=guests,
             created_by=request.user
         )
 
         return JsonResponse({'success': True})
    except Exception as e:
        print('Error', e)
 
        return JsonResponse({'success': False})
     
@api_view(['POST'])
def toggle_favorite(request, pk):
    property = Property.objects.get(pk=pk)
 
    if request.user in property.favorited.all():
        property.favorited.remove(request.user)
 
        return JsonResponse({'is_favorite': False})
    else:
        property.favorited.add(request.user)
 
        return JsonResponse({'is_favorite': True})