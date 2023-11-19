from django.shortcuts import render

def index(request):
    print("Index view called")
    return render(request, 'main/index.html')