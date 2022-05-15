from rest_framework import serializers
from .models import Listing, Bookings, reserved,Landlord


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
            'image_url1',
            'image_url2',
            'agent',
            'features',
            'requirement',
        )
        def update(self,serializer):
            serializer.save()
            serializer.instance.available()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserved
        fields = (
            'id',
            'Fullname',
            'house',
            'price',
            'room_type',
            'phone_number',
            'email',
            'house_name',
            'repetitioncheck',
            'confirmed'
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

# class ReservedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = reserved
#         fields = (
#             'id',
#             'Fullname',
#             'house',
#             'room_type',
#             'phone_number',
#             'email',
#         )