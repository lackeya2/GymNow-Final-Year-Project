from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, "pages/homepage.html")

def login_page(request):
    return render(request, "pages/login.html")


def contact_us(request):
    return render(request, "pages/contact.html")
