from django.contrib import admin
from .models import Listing,Booking,ConfirmedBookings,RoomType,Landlord

# Register your models here.

admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(ConfirmedBookings)
admin.site.register(RoomType)
admin.site.register(Landlord)
