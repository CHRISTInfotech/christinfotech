from django.urls import path
from adminPanel.views import dashboard, login

urlpatterns = [
    path('dashboard',dashboard,name="dashboard"),
    path('login',login,name="login"),
]