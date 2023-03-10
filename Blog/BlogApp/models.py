from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
# Create your models here.
class Profile(models.Model):  
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=12, null=True)
    batch=models.IntegerField(max_length=10,default=1990)
    course = models.CharField(max_length=100,choices=(('BTECH','BTECH'),('MCA','MCA'),('MTECH','MTECH'),('COMMERCE','COMMERCE'),('MTECH','MTECH'),('MSC','MSC')))
    image = models.ImageField(upload_to="BlogApp/images",default="",blank=True)

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):

    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,default="")
    content=RichTextField(blank=True,null=True)
    job_offer=models.CharField(max_length=100,choices=(('SUMMER INTERN','SUMMER INTERN'),('JOB','JOB'),('PPO','PPO'),('WINTER INTERN','WINTER INTERN')),default=1)
    company_name=models.CharField(max_length=200,default="")
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    year=models.IntegerField(default=0)
    count=models.IntegerField(default=0,null=True)
    

    def __str__(self):
        return self.title

class Bookm(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_id=models.ForeignKey(BlogPost, on_delete=models.CASCADE,blank=True,null=True)

    





