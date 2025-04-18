from django.contrib import admin
from user_app.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'USER PROFILE ADMIN'
    site_title = 'Admin Portal'
    index_title = 'Welcome to the Admin Dashboard'
    site_url = '/manage_user'
    
custom_admin_site = MyAdminSite(name='useradmin')

# Register your models here.
class UserModel(UserAdmin):
    list_display =['username','email']

custom_admin_site.register(CustomUser)
