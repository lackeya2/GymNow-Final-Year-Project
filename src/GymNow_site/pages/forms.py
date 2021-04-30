from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Enter Full Name')
    phone_number = forms.CharField(max_length=100, help_text='Phone Number')
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone_number', 'password1', 'password2']

 
class MembershipForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Your First Name')
    phone_number = forms.CharField(max_length=100, help_text='Phone Number')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super (MembershipForm , self ).save(commit=False)
        user.username = self.cleaned_data ['username']
        user.is_staff = True

        if commit :
            user.save()

        return user


class BusinessProfileForm(forms.ModelForm): 
    business_name = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Business Name',}))
    location = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Location',}))
    image = forms.ImageField()
    email = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'placeholder': 'Email',}))
    phone = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Phone'}))
    # available_bookings = forms.ModelMultipleChoiceField(
    #     queryset=Booking.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Business_Owner
        fields = ('business_name', 'location', 'image', 'email', 'phone')
