from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('login',views.login_handler,name='login_handler'),
    path('logout',views.logout_handler,name='logout_handler'),
    path("post/<int:post_id>",views.post,name="post"),
    
]