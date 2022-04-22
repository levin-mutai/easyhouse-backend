from django.urls import path

from .views import ListListings, ListLandlords, ListBookings, DetailListings, DetailBookings, DetailLandlords

urlpatterns =[
    path('api/v1/listings', ListListings.as_view(), name='Listings'),
    path('api/v1/listings/<int:pk>/', DetailListings.as_view(), name='Specific Listing'),

    path('api/v1/bookings', ListBookings.as_view(), name='bookings'),
    path('api/v1/bookings<int:pk>/', DetailBookings.as_view(), name='Specific Booking'),

    path('api/v1/landlords', ListLandlords.as_view(), name='Landlords'),
    path('api/v1/landlords<int:pk>/', DetailLandlords.as_view(), name='Specific Landlord'),

]