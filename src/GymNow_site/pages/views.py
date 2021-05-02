from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import *
from django.db.models import Q
import json
import datetime


# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items

    else:
        customerbooking = []
        items =[]
        cartItems = []

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


def contact_us(request):
    return render(request, "pages/contact.html")

def Enroll_business(request):
    return render(request, "pages/Enroll_business.html")


@login_required(login_url='login_page')
def cart(request):

    if request.user.is_authenticated:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
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
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items
    else:
        items =[]
        customerbooking = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'customerbooking':customerbooking, 'cartItems':cartItems}
    return render(request, 'pages/checkout.html', context)


def UpdateCart(request):
    data = json.loads(request.body)
    bookingId = data['bookingId']
    action = data['action']
    print('Action:', action)
    print('Booking:', bookingId)

    user = Customer.objects.get(user=request.user)
    booking = Booking.objects.get(id=bookingId)
    customer_booking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)

    bookingItem, created = BookingItem.objects.get_or_create(customerbooking=customer_booking, booking=booking)

    if action == 'add':
        bookingItem.quantity = (bookingItem.quantity + 1)
    elif action == 'remove':
        bookingItem.quantity = (bookingItem.quantity - 1)
        
    bookingItem.save()
    
    if bookingItem.quantity <= 0:
        bookingItem.delete()
        
    return JsonResponse('Booking was added', safe=False)


def UpdateBooking(request):
    data = json.loads(request.body)
    customerbookingId = data['customerbookingId']
    action = data['action']
    print('Action:', action)
    print('CustomerBooking:',customerbookingId)

    customerbooking = BookingItem.objects.get(id=customerbookingId)
    # bookingItem, created = BookingItem.objects.get_or_create(customerbooking=customerbooking)

    if action == 'Delete':
        customerbooking.delete()
        
    return JsonResponse('Booking was Deleted', safe=False)

@login_required(login_url='login_page')
def BusinessProfile(request):
    user = Customer.objects.get(user=request.user)
    business = Business_Owner.objects.get(business_owner=user)

    form = BusinessProfileForm(request.POST,  instance=user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {'user':user, 'business':business, 'form':form}

    return render(request, 'pages/BusinessProfile.html', context)



def available_bookings(request):
    if request.user.is_authenticated:
        available_bookings = Business_Owner.objects.all()
        myFilter = BusinessOwnerFilter(request.GET, queryset=available_bookings)
        available_bookings = myFilter.qs
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items

    else:
        available_bookings = Business_Owner.objects.all()
        myFilter = BusinessOwnerFilter(request.GET, queryset=available_bookings)
        available_bookings = myFilter.qs
        customerbooking = []
        items =[]
        cartItems = []

    context = {"available_bookings": available_bookings, "myFilter": myFilter ,'items':items, 'customerbooking':customerbooking, "cartItems":cartItems}
    return render(request, "pages/available_bookings.html", context )

@login_required(login_url='login_page')
def business_owners(request, pk):
    if request.user.is_authenticated:
        business_owners = Business_Owner.objects.filter(pk=pk)
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items

    else:
        business_owners = Business_Owner.objects.filter(pk=pk)
        customerbooking = []
        items =[]
        cartItems = []

    context = {"business_owners": business_owners, 'items':items, 'customerbooking':customerbooking, "cartItems":cartItems }
    return render(request, "pages/business_owners.html", context)



@login_required(login_url='login_page')
def customer(request):
    if request.user.is_authenticated:
        user = Customer.objects.get(user=request.user)
        lookup = {'customerbooking__complete': True, 'customerbooking__customer': user}
        customerbookings = BookingItem.objects.filter(**lookup)
        items = []
        cartItems = []
    else:
        customerbookings = []
        items =[]
        cartItems = []

    context = {'customer':customer, 'customerbookings':customerbookings, 'items':items, "cartItems":cartItems}

    return render(request, "pages/customer.html", context )

def completeOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        total = float(data['form']['total'])
        customerbooking.transaction_id = transaction_id
        
        if total == customerbooking.get_cart_total:
            customerbooking.complete = True
        customerbooking.save()

    else:
        print('User is not logged in')
    
    return JsonResponse('Payment Successful', safe=False)