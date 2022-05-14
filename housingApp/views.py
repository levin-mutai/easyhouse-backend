from django.shortcuts import render
from rest_framework import generics

from .models import Listing, reserved, Landlord
from .serializers import ListingSerializer, BookingSerializer, LandlordSerializer

# Create your views here.


class ListListings(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class DetailListings(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListBookings(generics.ListCreateAPIView):
    queryset = reserved.objects.all()
    serializer_class = BookingSerializer


class DetailBookings(generics.RetrieveUpdateDestroyAPIView):
    queryset = reserved.objects.all()
    serializer_class = BookingSerializer


class ListLandlords(generics.ListCreateAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer


class DetailLandlords(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

# class Reserves(generics.reateAPIView):
#     queryset = Landlord.objects.all()
#     serializer_class = LandlordSerializer