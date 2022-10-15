from django.shortcuts import render,redirect
from home.models import Internship
# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def internship(request):
    return render(request,'internship/internship.html')

def internshipForm(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        dob=request.POST['dob']
        institute=request.POST['institute']
        course=request.POST['course']
        areaofinterest=request.POST['areaofinterest']
        hours=request.POST['hours']
        resume=request.FILES['resume']

        object=Internship.objects.create(name=name,email=email,phoneno=phoneno,dob=dob,institute=institute,course=course,areaofinterest=areaofinterest,hours=hours,resume=resume)
        object.save()  
        return redirect('internshipForm')
    else :
        return render(request,'support/internshipForm.html')


def serviceForm(request):
    return render(request,'support/service.html')

def ourProduct(request):
    return render(request,'products/products.html')



