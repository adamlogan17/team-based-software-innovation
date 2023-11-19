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
