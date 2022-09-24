from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def internship(request):
    return render(request,'internship/internship.html')

def internshipForm(request):
    return render(request,'support/internshipForm.html')

def serviceForm(request):
    return render(request,'support/service.html')

def ourProduct(request):
    return render(request,'products/products.html')



