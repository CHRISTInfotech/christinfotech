from django.shortcuts import render,redirect
from adminPanel.models import Internship, Development, Newsletter
from django.contrib import messages
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == "POST":
        email_sub=request.POST['email'] 
        obj=Newsletter.objects.filter(email_sub=email_sub).count()
        if obj >= 1:
            messages.success(request, "You're already subscribed. Thank You!")    
            return redirect('main')
        else:
            Newsletter.objects.create(email_sub=email_sub)    
            messages.success(request, "Thank You for subscribing to our newsletter!")    
            return redirect('main')
    else:
        return render(request, 'home/index.html')

def internship(request):
    return render(request,'internship/internship.html')

def internshipForm(request):
    if request.method == "POST" and request.FILES:
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        dob=request.POST['dob']
        formatted_date = datetime.strptime(dob, '%d-%m-%Y').strftime('%Y-%m-%d')
        institute=request.POST['institute']
        course=request.POST['course']
        areaofinterest=request.POST['areaofinterest']
        hours=request.POST['hours']        
        resume=request.FILES['resume']
        object=Internship.objects.create(name=name,email=email,phoneno=phoneno,dob=formatted_date,institute=institute,course=course,areaofinterest=areaofinterest,hours=hours,resume=resume)
        object.save()  
        messages.success(request, "Request received, will get back to you soon. ")
        return redirect('internshipForm')
    

    elif request.method == "POST":
            name=request.POST['name']
            email=request.POST['email']
            phoneno=request.POST['phoneno']
            dob=request.POST['dob']
            formatted_date = datetime.strptime(dob, '%d-%m-%Y').strftime('%Y-%m-%d')
            # print(formatted_date)
            institute=request.POST['institute']
            course=request.POST['course']
            areaofinterest=request.POST['areaofinterest']
            hours=request.POST['hours']        

            object=Internship.objects.create(name=name,email=email,phoneno=phoneno,dob=formatted_date,institute=institute,course=course,areaofinterest=areaofinterest,hours=hours)
            object.save()  
            messages.success(request, "Request received, will get back to you soon. ")
            # messages.error(request, "Error: This is the sample error Flash message.")
            # post.save()
            return redirect('internshipForm')
    else :
        return render(request,'support/internshipForm.html')
    


def serviceForm(request):
    if request.method == "POST" and request.FILES:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        compinst=request.POST['compinst']
        department=request.POST['department']
        requestdesc=request.POST['requestdesc']
        document=request.FILES['document']

        object=Development.objects.create(fname=fname,lname=lname,phoneno=phoneno,email=email,compinst=compinst,department=department,requestdesc=requestdesc,document=document)
        object.save()
        messages.success(request, "Request received, will get back to you soon. ")
        return redirect('serviceForm')
    
    elif request.method == "POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            phoneno=request.POST['phoneno']
            email=request.POST['email']
            compinst=request.POST['compinst']
            department=request.POST['department']
            requestdesc=request.POST['requestdesc']

            object=Development.objects.create(fname=fname,lname=lname,phoneno=phoneno,email=email,compinst=compinst,department=department,requestdesc=requestdesc)
            object.save()
            messages.success(request, "Request received, will get back to you soon. ")
            return redirect('serviceForm')
    else :
        return render(request,'support/service.html')

def ourProduct(request):
    return render(request,'products/products.html')
    
def ourTeam(request):
    return render(request,'aboutus/aboutus.html')

    
