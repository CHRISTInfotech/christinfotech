from django.db import models
from django.utils import timezone

# Create your models here.
class Internship(models.Model):
    request_date = models.DateField(auto_now_add = True)   
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=10,null=True)
    dob=models.DateField(default=timezone.now,)
    institute=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    areaofinterest=models.CharField(max_length=50)
    hours=models.CharField(max_length=10)
    resume=models.FileField(upload_to="media")


class Development(models.Model):
    request_date = models.DateField(auto_now_add = True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=10,null=True)
    email=models.CharField(max_length=50)
    compinst=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    requestdesc= models.TextField(null=True)
    document=models.FileField(upload_to="media")
    
class Newsletter(models.Model):
    email_sub=models.EmailField(unique=True)