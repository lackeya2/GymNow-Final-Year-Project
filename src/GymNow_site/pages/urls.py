from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('login_page/', views.login_page),
    path('contact_us/', views.contact_us),
    path('bookings/', views.bookings),
    path('locations/', views.locations),
]
