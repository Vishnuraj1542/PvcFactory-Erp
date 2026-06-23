from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout

# Create your models here.
class UserAccount(AbstractUser):
    Usertype_choices=[('Admin','admin'),('HR','hr'),('Qc','qc'),('Manager','manager'),('Employees','employees'),]
    empid = models.CharField(max_length=12,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class PersonalDetails(models.Model):
    user = models.OneToOneField(UserAccount,null=True,blank=True)
    image=models.ImageField(upload_to='pictures')
    passport_number=models.IntegerField(null=True,blank=True)
    visa_number=models.CharField(max_length=50,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)