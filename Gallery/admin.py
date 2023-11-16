from django.contrib import admin
from . import models


# Register your models here.

class ShowGallery(admin.ModelAdmin):
    list_display = ["image", 'description', 'is_active']


admin.site.register(models.Gallery, ShowGallery)
