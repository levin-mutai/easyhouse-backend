from rest_framework import serializers
from .models import Listing, Booking, Landlord


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'id',
            'name',
            'description',
            'location',
            'house_type',
            'ratings',
            'verified',
            'image_url',
            'price',
            'landlord',
            'town',
            'availability',
            'units_available',
        )
        def update(self,serializer):
            serializer.save()
            serializer.instance.available()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'id',
            'Fullname',
            'house',
            'room_type',
            'phone_number',
            'email',
        )


class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )