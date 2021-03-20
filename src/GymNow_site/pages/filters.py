import django_filters

from .models import *

class BusinessOwnerFilter(django_filters.FilterSet):
    class Meta:
        model = Business_Owner
        fields ='__all__'
        exclude = ['image']
        
