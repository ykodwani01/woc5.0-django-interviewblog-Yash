from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import CreateUserForm
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request,'index.html')
def logout_handler(request):
    logout(request)
    return redirect('index')

def login_handler(request):

    if request.user.is_authenticated:
        return redirect('home')
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect (home)
        else:
            messages.info(request,"INVALID Password or Username")
            return render(request,'login.html')
    return render(request,'login.html')

@login_required(login_url='/login')
def home(request):
    return render(request,'blogpage.html')

def register(request):

    
    
    # if(request.method=="POST"):
    #     username=request.POST['email']
    #     email=request.POST['email']
    #     fname=request.POST['fname']
    #     course=request.POST['course']
    #     pass1=request.POST['password']
    #     num=request.POST['number']
    #     myuser=User.objects.create_user(username,email,pass1,course)
        
    #     myuser.first_name=fname
        
    #     myuser.save()
    #     return render(request,'index.html')
    form=CreateUserForm(request.POST)
    if(request.method=="POST"):
        if form.is_valid():
            user=form.save()
            user.batch=form.cleaned_data.get('batch')
            user.course=request.POST.get('course')

            user.contact_number=request.POST.get('contact_number')
            print(user)
            temp=Profile.objects.all()
            hello=Profile(user=user)
            hello.batch=user.batch
            hello.contact_number=user.contact_number
            hello.course=user.course
            hello.save()
            
            return redirect(index)
        else:
            messages.info(request,messages.INFO,'Please Enter in valid format')

    
    return render(request,'register.html',{'form':form})