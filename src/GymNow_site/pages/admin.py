from django.contrib import admin


# Register your models here.
from .models import *


admin.site.register(Customer)
admin.site.register(Business_Owner)
admin.site.register(Booking)
admin.site.register(CustomerBooking)
admin.site.register(Location)
admin.site.register(Business)
admin.site.register(BookingItem)
