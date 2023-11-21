from . import views
from django.urls import path
from .requestFunctions.accountHandling import verify

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('receive_message/', views.receive_message, name='receive_message'),
    path('settings/', views.settings, name='settings'),
    path('chat/', views.chat, name='chat'),
    path('journal/', views.journal, name='journal'),
    path('gallery/', views.gallery, name='gallery'),
    path('verify/', verify, name='verify'),
    path('login/', views.loginPage, name='login'),
]