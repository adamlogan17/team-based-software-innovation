from database.models import *
from mysite.settings import *
from .forms import CustomLoginForm
from django.shortcuts import render
from django.http import JsonResponse

'''
    @Author: @KyleMcComb
'''
def receive_message(request):
    return JsonResponse({'message': 'response from social worker'})

'''
    @Author: @KyleMcComb
    @Description: Renders the index.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def index(request):
    return render(request, 'index.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the chatPage.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def chat(request):
    return render(request, 'chatPage.html', {'form': CustomLoginForm()})


'''
    @Author: @DeanLogan
    @Description: Renders the settings.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def settings(request):
    return render(request, 'settings.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the journal.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def journal(request):
    return render(request, 'journal.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the gallery.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def gallery(request):
    return render(request, 'gallery.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the login.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def loginPage(request):
    from django.contrib import admin
    print(admin.site.urls)
    return render(request, 'login.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the 404.html file to be displayed to the user whenever they have navigated to a page that cannot be found.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def custom404(request, exception=None):
    return render(request, '404.html', status=404)