from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from BlogApp.models import BlogPost,Profile

admin.site.register(BlogPost)
admin.site.register(Profile)