from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('login',views.login_handler,name='login_handler'),
    path('search',views.search,name='search'),
    path('logout',views.logout_handler,name='logout_handler'),
    path('add',views.add,name="add"),
    path('bookmarks',views.show_bookmark,name='show_bookmark'),
    path('bookmark/<int:post_id>',views.bookmark,name='bookmark'),
    path('remove_bookmark/<int:post_id>',views.rem_bookmark,name='rem_bookmark'),
    path("post/<int:post_id>",views.post,name="post"),
    
    path("reset",auth_views.PasswordResetView.as_view()),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),   
    
]