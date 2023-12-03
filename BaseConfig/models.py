from django.db import models


# Create your models here.

class FooterData(models.Model):
    site_description = models.CharField(max_length=500, null=True, blank=True, verbose_name='توضیحات سایت')
    site_logo = models.ImageField(upload_to='footer/site_logo', null=True, blank=True, verbose_name='لوگوسایت')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='آدرس')
    location = models.CharField(max_length=500, null=True, blank=True, verbose_name='موقعیت در نقشه')
    phone_number = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن همراه')
    landline_phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن ثابت')
    instagram = models.CharField(max_length=200, null=True, blank=True, verbose_name='اینستاگرام')
    telegram = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلگرام')
    whatsapp = models.CharField(max_length=200, null=True, blank=True, verbose_name='واتس اپ')
    per_page_item = models.IntegerField(default=10, verbose_name='تعداد آگهی در هر صفحه')

    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        db_table = 'FooterData'
        verbose_name = 'تنطیمات عمومی سایت'
        verbose_name_plural = 'تنظیمات عمومی سایت'


class HomeData(models.Model):
    home_description = models.CharField(max_length=500, null=True, blank=True, verbose_name='توضیحات در صفحه اصلی')

    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        db_table = 'HomeData'
        verbose_name = 'اطلاعات صفحه اصلی'
        verbose_name_plural = 'اطلاعات صفحه اصلی'


class SliderImage(models.Model):
    image = models.ImageField(upload_to='Slider', verbose_name='تصویر اسلایدر')

    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        db_table = 'SliderImage'
        verbose_name = 'عکس اسلایدر'
        verbose_name_plural = 'عکس های اسلایدر'