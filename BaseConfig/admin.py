from django.contrib import admin
from BaseConfig import models


class showFooterData(admin.ModelAdmin):
    list_display = ['__str__', 'is_active', 'site_description', 'site_logo', 'address', 'phone_number']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


class showHomeData(admin.ModelAdmin):
    list_display = ['home_description', 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


class showSliderImage(admin.ModelAdmin):
    list_display = ['image', 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


admin.site.register(models.FooterData, showFooterData)
admin.site.register(models.HomeData, showHomeData)
admin.site.register(models.SliderImage, showSliderImage)
