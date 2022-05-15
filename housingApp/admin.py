from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Listing,Bookings,RoomType,Landlord, reserved


# class UserInline(admin.StackedInline):
#     model = userData
#     can_delete: False
#     verbose_name_plural: 'userData'

# class CustomUserAdmin (UserAdmin):
#     inlines = (AccountInline,)

# admin.site.unregister(User)
# admin.site.register(User,)

admin.site.site_header = "EasyHouse"
admin.site.register(Listing)
admin.site.register(reserved)
admin.site.register(Bookings)
admin.site.register(RoomType)
admin.site.register(Landlord)
admin.site.unregister(Group)
