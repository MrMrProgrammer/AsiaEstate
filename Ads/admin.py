from django.contrib import admin
from . import models


class ShowCategory(admin.ModelAdmin):
    list_display = ["fa_category", 'en_category']


class ShowLand(admin.ModelAdmin):
    list_display = ['__str__', 'size', 'address', 'priority']


class ShowVilla(admin.ModelAdmin):
    list_display = ["__str__", 'buildingSize', 'NumberOfRooms', 'address', 'priority']


class ShowApartment(admin.ModelAdmin):
    list_display = ["__str__", 'size', 'NumberOfRooms', 'floor', 'address', 'priority']


admin.site.register(models.Land, ShowLand)
admin.site.register(models.Villa, ShowVilla)
admin.site.register(models.Apartment, ShowApartment)
admin.site.register(models.Category, ShowCategory)
admin.site.register(models.Currency)
