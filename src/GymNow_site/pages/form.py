from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta
    model = User
    fields = ['usename', 'email', 'password1', 'password2']
 