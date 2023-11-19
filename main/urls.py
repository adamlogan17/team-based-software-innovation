from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('receive_message/', views.receive_message, name='receive_message'),
    path('chat/', views.chat, name='chat'),
]