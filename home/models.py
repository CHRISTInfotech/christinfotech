from django.db import models
from django.utils import timezone

# Create your models here.
class Internship(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=10,null=True)
    dob=models.DateField(default=timezone.now)
    institute=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    areaofinterest=models.CharField(max_length=50)
    hours=models.CharField(max_length=10)
    resume=models.FileField(upload_to="media")
