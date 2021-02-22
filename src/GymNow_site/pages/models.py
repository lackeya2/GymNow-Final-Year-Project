from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer_name

class Location(models.Model):
    LOCATION = (
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Donegal', 'Donegal'),
        ('Dublin', 'Dublin'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
        ('London', 'London')
        )
    
    name = models.CharField(max_length=200, null=True, choices=LOCATION)

    def __str__(self):
        return self.name



class Bookings(models.Model):
    CATEGORY = (
        ('Gym Booking', 'Gym Booking'),
        ('Personal Trainer', 'Personal Trainer'),
        ('Pilates', 'Pilates'),
        ('Yoga', 'Yoga'),
        ('Crossfit', 'Crossfit'),
        )

    time = models.CharField(max_length=200, null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR', default=0)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.category} {0.time} {0.price}' 
        return template.format(self)

class Business_Owner(models.Model):
    LOCATION = (
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Donegal', 'Donegal'),
        ('Dublin', 'Dublin'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
        )

    name = models.CharField(max_length=200, null=True)
    business_name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True, choices= LOCATION)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    available_bookings = models.ManyToManyField(Bookings)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        template = '{0.business_name}' 
        return template.format(self)

    class Meta:
        ordering = ['location']



class Customer_Bookings(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        )
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
    business_name = models.ForeignKey(Business_Owner, null=True, on_delete = models.CASCADE)
    booking = models.ForeignKey(Bookings, on_delete= models.CASCADE)
    order_status = models.CharField(max_length=300, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.customer} {0.business_name} {0.booking} {0.order_status}'
        return template.format(self)


# class CusotmerBookings(models.Model):
#     customer_name = modles.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
#     business_name = models.ForeignKey(Business_Owner, null=True, on_delete = models.CASCADE)
#     booking = models.ForeignKey(Bookings, on_delete= models.CASCADE)
#     order_status = models.ForeignKey(order_status)







