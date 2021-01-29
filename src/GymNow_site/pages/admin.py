from django.contrib import admin


# Register your models here.
from .models import *


admin.site.register(Customer)
admin.site.register(Business_Owner)
admin.site.register(Bookings)
admin.site.register(Bookings_Order)
admin.site.register(Location)
