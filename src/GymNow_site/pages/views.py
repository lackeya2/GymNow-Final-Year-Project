from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import BusinessOwnerFilter
from django.db.models import Q

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
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)


def customer_bookings(request):
    customer_bookings = Customer_Bookings.objects.all()
    return render(request, "pages/customer_bookings.html", {"customer_bookings":customer_bookings})

def available_bookings(request):
    available_bookings = Business_Owner.objects.all()
    myFilter = BusinessOwnerFilter(request.GET, queryset=available_bookings)
    available_bookings = myFilter.qs
    return render(request, "pages/available_bookings.html", {"available_bookings":available_bookings, "myFilter":myFilter}) 
    
def business_owners(request, pk):
    business_owners = Business_Owner.objects.filter(pk=pk)   
    return render(request, "pages/business_owners.html", {"business_owners":business_owners})



