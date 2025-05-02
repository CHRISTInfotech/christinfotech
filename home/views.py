from django.shortcuts import render, redirect
from adminPanel.models import Internship, Development, Newsletter
from django.contrib import messages
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == "POST":
        email_sub = request.POST.get('email')
        if email_sub:
            obj, created = Newsletter.objects.get_or_create(email_sub=email_sub)
            if not created:
                messages.info(request, "You're already subscribed. Thank You!")
            else:
                messages.success(request, "Thank you for subscribing to our newsletter!")
        else:
            messages.warning(request, "Please enter a valid email address.")
        return redirect('main')
    return render(request, 'home/index.html')

def internship(request):
    return render(request, 'internship/internship.html')


def internshipForm(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        dob = request.POST.get('dob')
        institute = request.POST.get('institute')
        course = request.POST.get('course')
        areaofinterest = request.POST.get('areaofinterest')
        hours = request.POST.get('hours')
        resume = request.FILES.get('resume')  # Will be None if not uploaded

        try:
            formatted_dob = datetime.strptime(dob, '%d-%m-%Y').strftime('%Y-%m-%d')
        except ValueError:
            messages.error(request, "Invalid date format. Please use DD-MM-YYYY.")
            return redirect('internshipForm')

        internship_obj = Internship.objects.create(
            name=name,
            email=email,
            phoneno=phoneno,
            dob=formatted_dob,
            institute=institute,
            course=course,
            areaofinterest=areaofinterest,
            hours=hours,
            resume=resume if resume else None
        )

        messages.success(request, "Request received, we'll get back to you soon.")
        return redirect('internshipForm')

    return render(request, 'support/internshipForm.html')


def serviceForm(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        compinst = request.POST.get('compinst')
        department = request.POST.get('department')
        requestdesc = request.POST.get('requestdesc')
        document = request.FILES.get('document')  # Can be None

        Development.objects.create(
            fname=fname,
            lname=lname,
            phoneno=phoneno,
            email=email,
            compinst=compinst,
            department=department,
            requestdesc=requestdesc,
            document=document if document else None
        )

        messages.success(request, "Request received, we'll get back to you soon.")
        return redirect('serviceForm')

    return render(request, 'support/service.html')

def ourProduct(request):
    return render(request, 'products/products.html')


def ourTeam(request):
    return render(request, 'aboutus/aboutus.html')
