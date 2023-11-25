from django.contrib import admin
from . import models


# Register your models here.

class ShowGallery(admin.ModelAdmin):
    list_display = ["__str__", 'description', 'is_active']
    list_editable = ['is_active']


class ShowGallerySetting(admin.ModelAdmin):
    list_display = ["pagination", 'is_active']
    list_editable = ['is_active']


admin.site.register(models.Gallery, ShowGallery)
admin.site.register(models.GallerySetting, ShowGallerySetting)