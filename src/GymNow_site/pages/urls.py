from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.LogOut, name='logout'),
    path('register_page/', views.register_page, name='register_page'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('Enroll_business/', views.Enroll_business, name='Enroll_business'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('membership_form/', views.membership_form, name='membership_form'),
    path('business_owners/<str:pk>/', views.business_owners, name='business_owners'),
    path('available_bookings/', views.available_bookings, name='available_bookings'),
    path('UpdateCart/', views.UpdateCart, name='UpdateCart'),
    path('customer/', views.customer, name='customer'),
    path('completeOrder/', views.completeOrder, name='completeOrder'),
    path('UpdateBooking/', views.UpdateBooking, name='UpdateBooking'),
    path('BusinessProfile/', views.BusinessProfile, name='BusinessProfile'),



]
