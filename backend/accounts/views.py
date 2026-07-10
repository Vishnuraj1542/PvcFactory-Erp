from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def checkviews(request):
    return HttpResponse('hello world')
