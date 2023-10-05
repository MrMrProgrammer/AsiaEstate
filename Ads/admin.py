from django.contrib import admin
from . import models


class ShowLand(admin.ModelAdmin):
    list_display = ['__str__', 'size', 'address', 'priority']
    # list_filter = [""]
    # list_editable = ["fields"]
    # list_filter = ["fields"]


class ShowVilla(admin.ModelAdmin):
    list_display = ["__str__", 'buildingSize', 'NumberOfRooms', 'address', 'priority']
    # list_filter = ["fields"]
    # list_editable = ["fields"]
    # list_filter = ["fields"]


class ShowApartment(admin.ModelAdmin):
    list_display = ["__str__", 'size', 'NumberOfRooms', 'floor', 'address', 'priority']
    # list_filter = ["fields"]
    # list_editable = ["fields"]
    # list_filter = ["fields"]


admin.site.register(models.Land, ShowLand)
admin.site.register(models.Villa, ShowVilla)
admin.site.register(models.Apartment, ShowApartment)
admin.site.register(models.Category)
