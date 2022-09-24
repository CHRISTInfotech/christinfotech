from django.urls import path, include

from home.views import index, internship, internshipForm, serviceForm, ourProduct

urlpatterns = [
    path('', index, name='main'),
    path('internship',internship,name='internship'),
    path('internshipForm',internshipForm,name='internshipForm'),
    path('serviceForm',serviceForm,name='serviceForm'),
    path('ourProduct',ourProduct,name='ourProduct'),
    
]
