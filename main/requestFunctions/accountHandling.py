# below imports are used for sending an email
import io
import json
import base64
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from database.models import *
from mysite.settings import *
from django.http import JsonResponse
from django.http import HttpResponse
from main.forms import CustomLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

"""
    @Author: @DeanLogan
    @Description: Verifies user authentication, including two-factor authentication (2FA) if enabled.
    @param: request - The HttpRequest object containing user authentication and 2FA information.
    @return: JsonResponse indicating whether the user is logged in ('true' or 'false') and any errors.
"""
def verify(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        
        # Check if the form is valid; if not, the user may have failed the captcha
        if form.is_valid():
            # Attempt to authenticate the user using provided username and password
            authenticatedUser = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
            # Log in the user if authentication is successful
            login(request, authenticatedUser)
            
            # Set session timeout based on 'remember_me' value
            if form.cleaned_data.get('remember_me', False):
                request.session.set_expiry(1209600)  # Two weeks (in seconds)
            
            return JsonResponse({'loggedIn': 'true'})  # User is successfully logged in
        
        else:
            return JsonResponse({'loggedIn': 'false', 'errors': 'Invalid credentials'})  # Captcha or credentials validation failed
    
    else:
        return JsonResponse({'errors': 'Invalid request method'})  # Invalid request method (not POST)

