from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, "pages/homepage.html")

def login_page(request):
# this function checks if the user is in database,
# once it finds the username and password in the database the user is logged in
# if the username or password is not found error messge presented 
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            messages.info(request, 'Password OR Username is Incorrect')


    return render(request, "pages/login.html")

def register_page(request):
# This saves and add a user to django database if they have entered a valid registration form, 
# also sends 1 time flash messege on succesful Account creation with users username
    RegForm = RegistrationForm()

    if request.method == 'POST':
        RegForm = RegistrationForm(request.POST)
        if RegForm.is_valid():
            RegForm.save()
            user = RegForm.cleaned_data.get('username')
            messages.success(request, 'User Account was created for ' + user )

            return redirect('login_page')

    context = {'RegForm': RegForm}
    return render(request, "pages/register.html", context)

def LogOut(request):
	logout(request)
	return redirect('login_page')

# only allows access to this page if user logged in
#  otherwise redirects to login page
@login_required(login_url='login_page')
def contact_us(request):
    return render(request, "pages/contact.html")


@login_required(login_url='login_page')
def bookings(request):
    bookings = Bookings.objects.all()
    return render(request, "pages/bookings.html", {"bookings":bookings})

def locations(request):
    locations = Location.objects.all()
    return render(request, "pages/locations.html", {"locations":locations})

# def customer_bookings(request):
#     customer_bookings = CustomerBookings.objects.all()
#     return render(request, "pages/customer_bookings.html", {"customer_bookings":customer_bookings})
