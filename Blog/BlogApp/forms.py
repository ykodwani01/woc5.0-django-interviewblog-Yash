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
    contact_number = forms.CharField(label='Contact Number',required=True) 
    course = forms.ChoiceField(label="Course", choices=[('BTECH','BTECH'),('MCA','MCA'),('MTECH','MTECH'),('COMMERCE','COMMERCE'),('MTECH','MTECH'),('MSC','MSC')], required=True)
    batch=forms.IntegerField(label="Batch",required=True)
    image=forms.ImageField(label="Your Image",required=False)
    

    class Meta:
        # User.username=User.email
        model = User
        fields=['username','first_name','email','batch','course','image','password1','password2']


class CreateNewPost(forms.Form):
    
    title=forms.CharField(label="Title")
    content=forms.CharField(label="Content")
    job_offer=forms.ChoiceField(label="Job Type",choices=((1,'Summer Intern'),(2,'Job'),(3,'PPO'),(4,'Winter Intern')))
    company_name=forms.CharField(label="Company")
    author=forms.CharField(label="Author")


class UpdateUserForm(forms.ModelForm):

    contact_number = forms.CharField(label='Contact Number',required=True) 
    course = forms.ChoiceField(label="Course", choices=[('BTECH','BTECH'),('MCA','MCA'),('MTECH','MTECH'),('COMMERCE','COMMERCE'),('MTECH','MTECH'),('MSC','MSC')], required=True)
    batch=forms.IntegerField(label="Batch",required=True)
    image=forms.ImageField(label="Your Image",required=False)
    class Meta:
        model=User
        fields=['first_name','batch','course','contact_number','image']


