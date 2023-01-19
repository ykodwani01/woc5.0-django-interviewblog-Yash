from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

class CreateUserForm(UserCreationForm):
    contact_number = forms.CharField(label='Contact Number') 
    course = forms.CharField(label='Course') 
    batch=forms.IntegerField(label="Batch")
    

    class Meta:
        model = User
        fields=['username','email','batch','course','password1','password2']
