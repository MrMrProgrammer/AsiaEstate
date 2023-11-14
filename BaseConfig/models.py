from django.db import models


# Create your models here.

class FooterData(models.Model):
    site_description = models.CharField(max_length=500, null=True, blank=True)
    site_logo = models.ImageField(upload_to='footer/site_logo', null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    landline_phone = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    per_page_item = models.IntegerField(default=10)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'FooterData'
        verbose_name = 'فوتر'
        verbose_name_plural = 'تنظیمات فوتر'


class HomeData(models.Model):
    home_description = models.CharField(max_length=500, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'HomeData'
        verbose_name = 'اطلاعات صفحه اصلی'
        verbose_name_plural = 'اطلاعات صفحه اصلی'


class SliderImage(models.Model):
    image = models.ImageField(upload_to='Slider')

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'SliderImage'
        verbose_name = 'عکس اسلایدر'
        verbose_name_plural = 'عکس های اسلایدر'
