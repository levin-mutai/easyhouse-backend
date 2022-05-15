
from django.urls import path,re_path,include

from .views import ListListings, ListLandlords, ListBookings, DetailListings, DetailBookings, DetailLandlords
from .router import reserve

urlpatterns =[
    path('api/v1/listings', ListListings.as_view(), name='Listings'),
    path('api/v1/listings/<int:pk>/', DetailListings.as_view(), name='Specific Listing'),

    path('api/v1/reserved', ListBookings.as_view(), name='bookings'),
    path('api/v1/reserved<int:pk>/', DetailBookings.as_view(), name='Specific Booking'),
    re_path('^api/', include(reserve.urls)),

    path('api/v1/landlords', ListLandlords.as_view(), name='Landlords'),
    path('api/v1/landlords<int:pk>/', DetailLandlords.as_view(), name='Specific Landlord'),

]