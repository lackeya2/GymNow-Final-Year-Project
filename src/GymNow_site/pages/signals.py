from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=User)
def Create_User_Profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
