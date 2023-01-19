from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if(request.method=="POST"):
        username=request.POST['email']
        email=request.POST['email']
        fname=request.POST['fname']
        course=request.POST['course']
        pass1=request.POST['password']
        num=request.POST['number']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        
        myuser.save()
        return render(request,'index.html')
    return render(request,'register.html')