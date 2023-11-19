from database.models import *
from mysite.settings import *
from .forms import CustomLoginForm
from django.shortcuts import render
from django.http import JsonResponse


'''
    @Author: @DeanLogan
    @Description: Renders the index.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def index(request):
    return render(request, 'index.html')

'''
    @Author: @DeanLogan
    @Description: Renders the chatPage.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def chat(request):
    return render(request, 'chatPage.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Returns an example response from a social worker to demonstrate how conversations between the two may work.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def receive_message(request):
    return JsonResponse({'message': 'response from social worker'})