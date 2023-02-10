from django.urls import path
from adminPanel.views import dashboard, login_admin, registrationTB, logout_request
from . import views

urlpatterns = [
    path('dashboard',dashboard,name="dashboard"),
    path('login',login_admin, name="login"),
    path('registrationTB',registrationTB,name="registrationTB"),
    path('logout', logout_request, name="logout"),
    
]