from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer_name

class Business_Owner(models.Model):
    name = models.CharField(max_length=200, null=True)
    business_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.business_name

class Bookings(models.Model):
    CATEGORY = (
        ('Gym Booking', 'Gym Booking'),
        ('Personal Trainer', 'Personal Trainer'),
        ('Pilates', 'Pilates'),
        ('Yoga', 'Yoga'),
        ('Crossfit', 'Crossfit'),
        )

    name = models.CharField(max_length=200, null=True)
    business_name = models.ForeignKey(Business_Owner, null=True, on_delete = models.CASCADE)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

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




