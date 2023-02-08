from django.shortcuts import render,redirect
from adminPanel.models import Internship, Development, Newsletter
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == "POST":
        email_sub=request.POST['email'] 
        obj=Newsletter.objects.filter(email_sub=email_sub).count()
        if obj >= 1:
            messages.success(request, "EmailID already exhists")    
            return redirect('main')
        else:
            Newsletter.objects.create(email_sub=email_sub)    
            messages.success(request, "Thank You for subscribing to our newletter!")    
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
        institute=request.POST['institute']
        course=request.POST['course']
        areaofinterest=request.POST['areaofinterest']
        hours=request.POST['hours']        
        resume=request.FILES['resume']
        object=Internship.objects.create(name=name,email=email,phoneno=phoneno,dob=dob,institute=institute,course=course,areaofinterest=areaofinterest,hours=hours,resume=resume)
        object.save()  
        messages.success(request, "Request received, will get back to you soon. ")
        return redirect('internshipForm')
    

    elif request.method == "POST":
            name=request.POST['name']
            email=request.POST['email']
            phoneno=request.POST['phoneno']
            dob=request.POST['dob']
            institute=request.POST['institute']
            course=request.POST['course']
            areaofinterest=request.POST['areaofinterest']
            hours=request.POST['hours']        
        
        # post=Internship()
        # post.name=request.POST['name']
        # post.email=request.POST['email']
        # post.phoneno=request.POST['phoneno']        
        # post.dob=request.POST['dob']
        # post.institute=request.POST['institute']
        # post.course=request.POST['course']
        # post.areaofinterest=request.POST['areaofinterest']
        # post.hours=request.POST['hours']
        # post.resume=request.FILES['resume']

            object=Internship.objects.create(name=name,email=email,phoneno=phoneno,dob=dob,institute=institute,course=course,areaofinterest=areaofinterest,hours=hours)
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

# def newsLetter(request):
#     if request.method == "POST":
#         email_sub=request.POST['email']
        
#         Newsletter.objects.create(email_sub=email_sub)
        
#         return redirect()
    # if request.method == "POST":
    #     if request.POST['email'] != "":
    #         email_sub=request.POST['email']        
    #         Newsletter.objects.create(email_sub=email_sub)        
    #         return redirect('main')
    #     else:
    #         return render(request, 'home/index.html')
    # else:
    #     return render(request, 'home/index.html')


