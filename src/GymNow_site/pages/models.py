from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.user}'
        return template.format(self)

    @property
    def customerbookings(self):
        return self.name

@receiver(post_save, sender=User)
def Create_User_Profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()

	

class Member(models.Model):
    member_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.member_name

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

class Business(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    CATEGORY = (
        ('Gym Booking', 'Gym Booking'),
        ('Personal Trainer', 'Personal Trainer'),
        ('Pilates', 'Pilates'),
        ('Yoga', 'Yoga'),
        ('Crossfit', 'Crossfit'),
        )

    time = models.CharField(max_length=200, null=True)
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.CharField(max_length=200, null=True)

    def __str__(self):
        template = '{0.business}   {0.rating} ★   {0.category} {0.time}   € {0.price} '
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

    CATEGORY = (
        ('Gym Booking', 'Gym Booking'),
        ('Personal Trainer', 'Personal Trainer'),
        ('Pilates', 'Pilates'),
        ('Yoga', 'Yoga'),
        ('Crossfit', 'Crossfit'),
        )

    name = models.CharField(max_length=200, null=True)
    business_name = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, null=True, choices= LOCATION)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    available_bookings = models.ManyToManyField(Booking)
    image = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    

    def get_absolute_url(self):
        return reverse("business_owners", kwargs={"pk": self.pk})

    def __str__(self):
        template = '{0.business_name}' 
        return template.format(self)

    class Meta:
        ordering = ['location']

class CustomerBooking(models.Model):
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        template = '{0.customer}'
        return template.format(self)
    
    @property
    def cardPayment(self):
        cardpayment = False
        return cardpayment

    @property
    def get_cart_total(self):
        bookingitems = self.bookingitem_set.all()
        total = sum([item.get_total for item in bookingitems])
        return total

    @property
    def get_cart_items(self):
        bookingitems = self.bookingitem_set.all()
        total = sum([item.quantity for item in bookingitems])
        return total


class BookingItem(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    customerbooking = models.ForeignKey(CustomerBooking, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        template = '{0.customerbooking} {0.booking} Quantity {0.quantity}' 
        return template.format(self)
    
    @property
    def get_total(self):
        total = self.booking.price * self.quantity
        return total

    
    







