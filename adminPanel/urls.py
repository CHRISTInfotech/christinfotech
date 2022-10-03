from django.urls import path
from adminPanel.views import dashboard, login, registrationTB

urlpatterns = [
    path('dashboard',dashboard,name="dashboard"),
    path('login',login,name="login"),
    path('registrationTB',registrationTB,name="registrationTB"),
]