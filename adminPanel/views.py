from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout  #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Internship, Development, Newsletter

# Create your views here.

@login_required
def dashboard(request):
		query_results = Internship.objects.all() # Collect all records from table 
		dev_res = Development.objects.all()
		sub_res = Newsletter.objects.all()
		
		return render(request,'adminPanel/dashboard.html',context={'qr':query_results, 'dev_r':dev_res, 'email_r':sub_res})

# def login(request):
#     return render(request,'adminPanel/login.html')

def registrationTB(request):
    return render(request,'adminPanel/registration_tb.html')

#Login view function

# def login(request):    
#     if request.method == "POST":
#         username=request.POST['username']
#         password=request.POST['password']

#         user=authenticate(request,username=username,password=password)
      
#         if user is not None:
#             login(request,user)
#             # return HttpResponseRedirect('/AdminPanel/verification/')
#             return redirect("dashboard")

#         else:
#             # return redirect("signup")
#             return render(request, "AdminPanel/login.html")


#     else :
#         return render(request,'AdminPanel/login.html')

def login_admin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()

	return render(request,'AdminPanel/login.html')

def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.")
    return redirect("login")
	# logout(request)
    
	# messages.info(request, "You have successfully logged out.") 
    
	# return render(request,'AdminPanel/login.html')