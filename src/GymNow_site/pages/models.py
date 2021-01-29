from django.db import models

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

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    location = models.ForeignKey(Location, null=True, on_delete = models.CASCADE)
    description = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

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
    available_bookings = models.ForeignKey(Bookings, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

class Bookings_Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        )
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
    business_name = models.ForeignKey(Business_Owner, null=True, on_delete = models.CASCADE)
    booking = models.ForeignKey(Bookings, on_delete= models.CASCADE)
    order_status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)






