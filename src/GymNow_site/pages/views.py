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



# The following views were constructed with aids of the following youtube paylist and stackoverflow solutions
# These have been edited and taoilered to our models, attributes and variable names:

# https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO
# https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng


def homepage(request):
        # this get the objects within the CustomerBooking model whose customer attribute is = to the logged in User
        # if no customer booking exsist one is created
        # get all the bookingitems within the customer booking one customer booking can have mulple booking items i.e multple times or multple quantitys which is used to give relevant cart data according to the logged in customer
        # this code is repeated in any view who page contains a cart
    if request.user.is_authenticated:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(
            customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items

    else:
        customerbooking = []
        items = []
        cartItems = []

    context = {'items': items, 'customerbooking': customerbooking,
        'cartItems': cartItems}
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
    # enters form data from membership form into forms.py, if the data is valid the form is saved
    # Succesful messege is then printed and user redirected to login page to login to member account
    MemForm = MembershipForm()

    if request.method == 'POST':
        MemForm = MembershipForm(request.POST)
        if MemForm.is_valid():
            MemForm.save()
            user = MemForm.cleaned_data.get('username')
            messages.success(
                request, 'Membership Account was created for ' + user)

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

# only allows access to this page if user logged in
#  otherwise redirects to login page
@login_required(login_url='login_page')
def Enroll_business(request):
    return render(request, "pages/Enroll_business.html")


@login_required(login_url='login_page')
def cart(request):
    # same functionality as stated in homepage view
    if request.user.is_authenticated:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(
            customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items
    else:
        items = []
        customerbooking = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'customerbooking': customerbooking,
        'cartItems': cartItems}
    return render(request, 'pages/cart.html', context)


@login_required(login_url='login_page')
def checkout(request):
    # If a user is staff i.e a member the member checkout template is returned
    # Else normal checkout template is returned which requires credit card payment
    if request.user.is_staff:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items
        return render(request, 'pages/membership_checkout.html', {'items': items, 'customerbooking': customerbooking, 'cartItems': cartItems})
    else:
        user = Customer.objects.get(user=request.user)
        customerbooking, created = CustomerBooking.objects.get_or_create(customer=user, complete=False)
        items = customerbooking.bookingitem_set.all()
        cartItems = CustomerBooking.get_cart_items
        return render(request, 'pages/checkout.html',{'items':items, 'customerbooking':customerbooking, 'cartItems':cartItems})


def UpdateCart(request):
# json data imported from cart.html using shoopingcart.js
# bookingId allows us to track the excat booking and get its corrsponding data like price, business, time etc
# Bookingitem is made up of the a booking
# if the action imported is add the booking quantity increases by one, increasing the price
# if the action imported is remove the booking qunatity decreases by on untill qauntity = 0 where the booking is then removed from the users cart

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
# json data imported from customer wallet page(customer.html) using shopping cart.js
# if action is delete customer booking is deleted and removed from users wallet
    data = json.loads(request.body)
    customerbookingId = data['customerbookingId']
    action = data['action']
    print('Action:', action)
    print('CustomerBooking:',customerbookingId)

    customerbooking = BookingItem.objects.get(id=customerbookingId)

    if action == 'Delete':
        customerbooking.delete()
        
    return JsonResponse('Booking was Deleted', safe=False)

@login_required(login_url='login_page')
def BusinessProfile(request):
    # This view gets A business objects who have the logged in user as their business Owner
    # This then allows the user to edit the objects via the Business Profile Form
    # If the form is valid the business is updated and saved
    user = Customer.objects.get(user=request.user)
    business = Business_Owner.objects.get(business_owner=user)

    form = BusinessProfileForm(request.POST or None, request.FILES or None, instance=business)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {'user':user, 'confirm':confirm, 'business':business, 'form':form}

    return render(request, 'pages/BusinessProfile.html', context)



def available_bookings(request):
    # this view returns all business owner objects, these objects can then be filtered by the user using the BusinessOwnerFiler found in filter.py
    # The objects which can be filtered are business location and category
    # included is cart functionlity as previously stated
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
    # this view uses requests the primary key of a Business, it uses objects.filter to get the objects of the business owner model associated to requested primary key
    # Includes cart functionality
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
    # this view returns succesfully completed order who have the logged in user assinged to the customer booking
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
    # this view pulls JSON data when comfirm-payment button is press on checkout pages
    # it checks if the total pulled when the button was clciked is the same as the total in the users cart
    # if their equal the complete atrribute in customerbooking is set to true and will now show up in the users wallet
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
