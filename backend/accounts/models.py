from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout

# Create your models here.
class UserAccount(AbstractUser):
    usertype_choices=[('admin','Admin',),('HR','hr'),('Qc','qc'),('Manager','manager'),('Employees','employees'),]
    user_type=models .CharField(max_length=30,null=True,blank=True,choices=usertype_choices)
    empid = models.CharField(max_length=12,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    

class PersonalDetails(models.Model):
    accomodation_type = [('Company','company'),('Self','self')]
    user = models.OneToOneField(UserAccount,null=True,blank=True,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,null=True,blank=True)
    image=models.ImageField(upload_to='pictures',null=True,blank=True)
    passport_number=models.CharField(max_length=20,null=True,blank=True)
    visa_number=models.CharField(max_length=50,null=True,blank=True)
    accomodation = models.CharField(max_length=22,null=True,blank=True,choices=accomodation_type)
    created_at=models.DateTimeField(auto_now_add=True)

