from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout

# Create your models here.
class UserAccount(AbstractUser):
    Usertype_choices=[('Employees','employess'),('Workers','workers')]
    empid = models.CharField(max_length=12,unique=True)
    Name = models.CharField(max_length=30,)
    