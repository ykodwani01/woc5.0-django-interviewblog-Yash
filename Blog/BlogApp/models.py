from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):  
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=12, null=True)
    batch=models.IntegerField(max_length=10,default=1990)
    course = models.CharField(max_length=100,choices=(('BTECH','BTECH'),('MCA','MCA'),('MTECH','MTECH'),('COMMERCE','COMMERCE'),('MTECH','MTECH'),('MSC','MSC')))
    

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):

    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=5000)



