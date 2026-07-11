from django.contrib import admin
from .models import UserAccount,PersonalDetails

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(PersonalDetails)
