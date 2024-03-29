"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from users import views
#import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'))
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('names/', views.get_all_names, name= 'all_names'),
    path('names/1/', views.get_name_by_id, name='name_by_id'),
    path(r'name/1/', views.delete_name_by_id, name='delete_name'),
    path('postname/', views)

    ## I tried the following url but i get an error
    #path('name/<int:id>/', views.delete_name_by_id, name='delete_name'), 
    #path('names/<int:id>/', views.get_name_by_id, name='name_by_id')
   
]
'''
