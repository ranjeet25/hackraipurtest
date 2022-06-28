"""hack_raipur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from hack_raipur.views import main_page
from hack_raipur.views import map_page
from hack_raipur.views import analysis




urlpatterns = [

    
    path('admin/', admin.site.urls),
    path('', main_page), 
    path('map/', map_page), 
    path('visual/', analysis.as_view(), name='analysis'),
    
   
]
