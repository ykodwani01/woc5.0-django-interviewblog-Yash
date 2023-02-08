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
from django.db.models import Q
from .forms import *


# Create your views here.

def index(request):
    return render(request,'index.html')
def logout_handler(request):
    logout(request)
    return redirect('index')

def login_handler(request):

    if request.user.is_authenticated:
        return redirect('profile')
        
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect (profile)
        else:
            messages.info(request,"INVALID Password or Username")
            return render(request,'login.html')
    return render(request,'login.html')

@login_required(login_url='/login')
def profile(request):
    # print(User)
    
    temp=Profile.objects.get(user=request.user.id)
    # print(temp)
    b=temp.batch
    c=temp.course
    i=temp.image
    print(b)
    params={'b':b,'c':c,'i':i}


    return render(request,'dashboard.html',params)


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
    form=CreateUserForm(request.POST,request.FILES)

    
    if(request.method=="POST"):
        #print(request.POST)
        
        if form.is_valid():
            # user.email=user

            user=form.save()
            user.batch=form.cleaned_data.get('batch')
            user.course=request.POST.get('course')
            user.image=form.cleaned_data.get('image')
            print(user.image)
            #user.email=form.cleaned_data('email')
            user.contact_number=request.POST.get('contact_number')
            print(request.POST)
            amp=User.objects.get(username=user)
            amp.email=amp.username
            amp.save()
            

            temp=Profile.objects.all()
            hello=Profile(user=user)
            hello.batch=user.batch
            hello.contact_number=user.contact_number
            hello.course=user.course
            hello.image=user.image
            hello.save()
            
            return redirect(index)
        else:
            messages.info(request,messages.INFO,'Please Enter in valid format')

    
    return render(request,'register.html',{'form':form})



@login_required(login_url='/login')
def home(request):
    a=Bookm.objects.all()
    for i in a:
        i.post_id.count=i.post_id.count+1
        i.post_id.save()
        #print(i.post_id.count)
    b=BlogPost.objects.all()
    #print("hello")
    #print(b[4].count)
    temp=BlogPost.objects.all().order_by('-count')
    params={'posts': temp}
    return render(request,'blogpage.html',params)

@login_required(login_url='/login')
def post(request,post_id):
    temp=BlogPost.objects.filter(post_id=post_id)
    print(temp)
    params={'posts': temp[0]}   
    return render(request,'post.html',params)




@login_required(login_url='/login')
def add(request):
    
    
    if request.method=="POST":
        #print(request.user)
        title=request.POST.get('title')
        content=request.POST.get('content')
        company=request.POST.get('company')
        print("hello")
        job_type=request.POST.get('job_type')
        print(job_type)
        year=request.POST.get('year')
        if job_type=="WINTER INTERN":
            a=3
        if job_type=="JOB":
            a=1
        if job_type=="SUMMER INTERN":
            a=0
        if job_type=="PPO":
            a=2
        print(a)
        temp=request.user
        hello=BlogPost(title=title,content=content,company_name=company,author=temp,job_offer=a,year=year)
        hello.save()

        messages.info(request," Post Published")

    return render(request,'add_post.html')


def search(request):
    query=request.GET.get('query')
    posts=BlogPost.objects.filter(title__icontains=query) | BlogPost.objects.filter(company_name__icontains=query) 

    params={ 'posts' : posts }
    return render(request,'search_results.html',params)

@login_required(login_url='/login')
def show_bookmark(request):

    # if(request.method=='POST'):
    #     t=
    a=request.user
    b=Bookm.objects.filter(user_id=a)
    params={'posts':b}
    return render(request,'bookmarks.html',params)

def bookmark(request,post_id):
    c=BlogPost.objects.get(post_id=post_id)
    # print(c)
    if(Bookm.objects.filter(post_id=c,user_id=request.user)).exists():
        return redirect('show_bookmark')
    temp=Bookm(user_id=request.user,post_id=c)
    temp.save()
    return redirect('show_bookmark')

def rem_bookmark(request,post_id):
    Bookm.objects.filter(post_id=post_id,user_id=request.user).delete()
    return redirect('show_bookmark')

def mypost(request):
    posts=BlogPost.objects.filter(author=request.user)
    # print(a)
    params={'posts':posts}
    return render(request,'mypost.html',params)

def dele(request,post_id):
    BlogPost.objects.filter(author=request.user,post_id=post_id).delete()
    return redirect('home')

def edit(request,post_id):
    a=BlogPost.objects.get(author=request.user,post_id=post_id)
    params={'a':a}
    if request.method=='POST':
        
        title=request.POST.get('title')
        content=request.POST.get('content')
        company=request.POST.get('company')
        
        job_type=request.POST.get('job_type')
        year=request.POST.get('year')
        if job_type=="WINTER INTERN":
            a=3
        if job_type=="JOB":
            a=1
        if job_type=="SUMMER INTERN":
            a=0
        if job_type=="PPO":
            a=2
        
        temp=BlogPost.objects.filter(post_id=post_id).update(title=title,content=content,company_name=company,year=year,job_offer=a)
        return redirect('home')
        
    return render(request,'edit_page.html',params)

def edit_profile(request):
    user=request.user
    form = UpdateUserForm(initial={
        'first_name': user.first_name,
        'course': user.profile.course,
        'batch': user.profile.batch,
        'image': user.profile.image,
        'contact_number': user.profile.contact_number,
    })

    if(request.method=='POST'):

        form=UpdateUserForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            first_name = form.cleaned_data.get('first_name')
            contact_number = form.cleaned_data.get('contact_number')
            batch = form.cleaned_data.get('batch')
            course = form.cleaned_data.get('course')
            image=form.cleaned_data.get('image')

            pr=Profile.objects.get(user=request.user)
            pr.batch=batch
            pr.course=course
            pr.image=image
            
            pr.contact_number=contact_number
            user.first_name = first_name
            user.save()
            pr.save()
            return redirect('profile')
    return render(request,'editprofile.html',{'form':form})


