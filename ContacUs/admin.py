from django.contrib import admin
from . import models


# Register your models here.

class ShowMessage(admin.ModelAdmin):
    list_display = ["__str__", 'phone_number', 'message', 'datetime']


admin.site.register(models.ContactUs, ShowMessage)