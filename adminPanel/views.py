from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'adminPanel/dashboard.html')

def login(request):
    return render(request,'adminPanel/login.html')

def registrationTB(request):
    return render(request,'adminPanel/registration_tb.html')