from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def homepage(request):
    return render(request, "pages/homepage.html")

def login_page(request):
    return render(request, "pages/login.html")


def contact_us(request):
    return render(request, "pages/contact.html")

def bookings(request):
    bookings = Bookings.objects.all()
    return render(request, "pages/bookings.html", {"bookings":bookings})

def locations(request):
    locations = Location.objects.all()
    return render(request, "pages/locations.html", {"locations":locations})
