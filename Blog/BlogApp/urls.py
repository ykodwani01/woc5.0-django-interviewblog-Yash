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
    path('accounts/login/',views.login_handler,name="redirect"),
    path('login',views.login_handler,name='login_handler'),
    path('search',views.search,name='search'),
    path('logout',views.logout_handler,name='logout_handler'),
    path('add',views.add,name="add"),
    path('mypost',views.mypost,name="mypost"),
    path('bookmarks',views.show_bookmark,name='show_bookmark'),
    path('bookmark/<int:post_id>',views.bookmark,name='bookmark'),
    path('edit/<int:post_id>',views.edit,name='edit'),
    path('editprofile',views.edit_profile,name="edit_profile"),
    path('remove_bookmark/<int:post_id>',views.rem_bookmark,name='rem_bookmark'),
    path("post/<int:post_id>",views.post,name="post"),
    path('del/<int:post_id>',views.dele,name="dele"),
    path('report/<int:pid>',views.report,name="report"),


    

    #password forgot urls
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
  
    #change password
    path('change_password/',auth_views.PasswordChangeView.as_view(success_url='/home'),name="changepass"),
    path('change_password_done/',auth_views.PasswordChangeDoneView.as_view(),name="changepassdone"),

]