from rest_framework import serializers
 
 from .models import Property, Reservation
 
 
 
 
 class PropertiesListSerializer(serializers.ModelSerializer):
     class Meta:
         model = Property
         fields = (
             'id',
             'title',
             'price_per_night',
             'image_url',
         )
 
 
 class PropertiesDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model = Property
         fields = (
             'id',
             'title',
             'description',
             'price_per_night',
             'image_url',
             'bedrooms',
             'bathrooms',
             'guests',
             'landlord'
         )