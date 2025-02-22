"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from mysite.admin import customAdminSite
from main.views import *

handler404 =  custom404 # comment this line out if you want to see the old 404 page that displayed error info

# Register your custom admin site
admin.site = customAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('settings/', settings),
    path('', include("django.contrib.auth.urls")),
    re_path(r'^.*/$', custom404), # comment this line out if you want to see the old 404 page that displayed error info
]

admin.site.site_header = "Administration"
admin.site.site_title = "Administration"