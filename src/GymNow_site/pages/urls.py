from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.LogOut, name='logout'),
    path('register_page/', views.register_page, name='register_page'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('bookings/', views.bookings, name='bookings'),
    path('locations/', views.locations, name='locations'),
    path('customer_bookings/', views.customer_bookings, name='customer_bookings'),
    path('business_owners/', views.business_owners, name='business_owners'),

]
