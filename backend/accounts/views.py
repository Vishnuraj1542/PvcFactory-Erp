from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import UserAccount,PersonalDetails
from django.contrib.auth import authenticate
# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        username=request.Post.get('username')
        password=request.Post.get('Password')
        details= UserAccount.objects.get(username=username,password=password)
        if details is not None:
            authenticate(details)

