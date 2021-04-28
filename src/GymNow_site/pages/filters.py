import django_filters
from django_filters import CharFilter

from .models import *

class BusinessOwnerFilter(django_filters.FilterSet):
    location = CharFilter(field_name="location", lookup_expr='icontains')
    category = CharFilter(field_name="category", lookup_expr='icontains')
    class Meta:
        model = Business_Owner
        fields = ['location', 'category' ]
        exclude = ['image', 'name', 'business_name', 'email', 'phone']

class CustomerBookingFilter(django_filters.FilterSet):
	class Meta:
		model = CustomerBooking
		fields = '__all__'
        
