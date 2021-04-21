from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .forms import MembershipForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import BusinessOwnerFilter
from django.db.models import Q
import json

# Create your views here.


def homepage(request):
    customer = request.user.customer
    customerbooking, created = CustomerBooking.objects.get_or_create(customer=customer, complete=False)
    items = customerbooking.bookingitem_set.all()
    cartItems = CustomerBooking.get_cart_items

    context = {'items':items, 'customerbooking':customerbooking, 'cartItems':cartItems}
    return render(request, "pages/homepage.html", context)


def login_page(request):
    # this function checks if the user is in database,
    # once it finds the username and password in the database the user is logged in
    # if the username or password is not found error messge presented
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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
            messages.success(request, 'User Account was created for ' + user)

            return redirect('login_page')

    context = {'RegForm': RegForm}
    return render(request, "pages/register.html", context)


def membership_form(request):
    MemForm = MembershipForm()

    if request.method == 'POST':
        MemForm = MembershipForm(request.POST)
        if MemForm.is_valid():
            MemForm.save()
            user = MemForm.cleaned_data.get('username')
            messages.success(
                request, 'Mmebership Account was created for ' + user)

            return redirect('login_page')

    context = {'MemForm': MemForm}
    return render(request, "pages/membership_form.html", context)


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

    if request.user.is_authenticated:
        customer = request.user.customer
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=customer, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items
    else:
        items =[]
        customerbooking = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'customerbooking':customerbooking, 'cartItems':cartItems}
    return render(request, 'pages/cart.html', context)

@login_required(login_url='login_page')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=customer, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items
    else:
        items =[]
        customerbooking = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'customerbooking':customerbooking, 'cartItems':cartItems}
    return render(request, 'pages/checkout.html', context)


def UpdateBooking(request):
    data = json.loads(request.body)
    bookingId = data['bookingId']
    action = data['action']
    print('Action:', action)
    print('Booking:', bookingId)

    customer = request.user.customer
    booking = Booking.objects.get(id=bookingId)
    customer_booking, created = CustomerBooking.objects.get_or_create(customer=customer, complete=False)

    bookingItem, created = BookingItem.objects.get_or_create(customer_booking=customer_booking, booking=booking)

    if action == 'add':
        bookingItem.quantity = (bookingItem.quantity + 1)
    elif action == 'remove':
        bookingItem.quantity = (bookingItem.quantity - 1)
        
    bookingItem.save()
    
    if bookingItem.quantity <= 0:
        bookingItem.delete()
        
    return JsonResponse('Booking was added', safe=False)


def available_bookings(request):
    available_bookings = Business_Owner.objects.all()
    myFilter = BusinessOwnerFilter(request.GET, queryset=available_bookings)
    available_bookings = myFilter.qs
    customer = request.user.customer
    customerbooking, created = CustomerBooking.objects.get_or_create(customer=customer, complete=False)
    items = customerbooking.bookingitem_set.all()
    cartItems = CustomerBooking.get_cart_items

    context = {"available_bookings": available_bookings, "myFilter": myFilter ,'items':items, 'customerbooking':customerbooking, "cartItems":cartItems}
    return render(request, "pages/available_bookings.html", context )


def business_owners(request, pk):
    business_owners = Business_Owner.objects.filter(pk=pk)
    customer = request.user.customer
    customerbooking, created = CustomerBooking.objects.get_or_create(customer=customer, complete=False)
    items = customerbooking.bookingitem_set.all()
    cartItems = CustomerBooking.get_cart_items

    context = {"business_owners": business_owners, 'items':items, 'customerbooking':customerbooking, "cartItems":cartItems }
    return render(request, "pages/business_owners.html", context)
