from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import UserAccount,PersonalDetails

# Create your views here.
def checkviews(request):
    items=[{id:1,'name':'vishnuraj','designation':'electrician'},{id:2,'name':'gopi','occupation':'helper'}]
    return HttpResponse(items)
def UserDetails(request):
    details = list(PersonalDetails.objects.all())
    return JsonResponse(details,Safe=False)


