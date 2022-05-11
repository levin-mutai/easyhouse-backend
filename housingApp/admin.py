from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Listing,Booking,ConfirmedBookings,RoomType,Landlord

# Register your models here.
admin.site.site_header = "EasyHouse"
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(ConfirmedBookings)
admin.site.register(RoomType)
admin.site.register(Landlord)
admin.site.unregister(Group)
