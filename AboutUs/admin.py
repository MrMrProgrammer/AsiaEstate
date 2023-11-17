from django.contrib import admin
from . import models


class ShowAboutUs(admin.ModelAdmin):
    list_display = ["__str__", 'image', 'is_active', 'header_1', 'body_1', 'header_2', 'body_2', 'header_3', 'body_2']
    list_editable = ['is_active']


admin.site.register(models.AboutUs, ShowAboutUs)
