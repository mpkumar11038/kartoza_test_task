
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_app.admin import custom_admin_site
from . import views

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('base/', views.base, name='base'),
    path('', views.custom_login, name='login'),
    path('do_login', views.do_login, name='do_login'),
    path('do_logout', views.do_logout, name='logout'),
    
    path('manage_user', views.manage_users, name='manage_users'),
    path('edit_user/<str:id>', views.edit_user_profile, name='edit_user'),
    path('map', views.map, name='map')  

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)