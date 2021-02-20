from django.contrib import admin


# Register your models here.
from .models import *


admin.site.register(Customer)
admin.site.register(Business_Owner)
admin.site.register(Bookings)
admin.site.register(Customer_Bookings)
admin.site.register(Location)
