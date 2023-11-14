from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import pytz
from jdatetime import datetime as jdatetime

class Currency(models.Model):
    currency = models.CharField(max_length=20, verbose_name='واحد پول')

    class Meta:
        db_table = 'Currency'
        verbose_name = 'واحد پولی'
        verbose_name_plural = 'واحد های پولی'

    def __str__(self):
        return self.currency

class Category(models.Model):
    fa_category = models.CharField(max_length=20, verbose_name='نوع آگهی (فارسی)')
    en_category = models.CharField(max_length=20, verbose_name='نوع آگهی (انگلیسی)')

    class Meta:
        db_table = 'Category'
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌ ها'

    def __str__(self):
        return self.fa_category


class Land(models.Model):

    fa_db_name = models.CharField(max_length=20, editable=False, default='زمین', verbose_name='نام جدول (فارسی)')
    en_db_name = models.CharField(max_length=20, editable=False, default='Land', verbose_name='نام جدول (انگلیسی)')

    title = models.CharField(max_length=200, verbose_name='عنوان')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')

    size = models.IntegerField(blank=True, null=True, verbose_name='متراژ زمین')

    adaptive = models.BooleanField(default=False, verbose_name='آیا قیمت توافقی است ؟')

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True, verbose_name='واحد پول')

    PricePerMeter = models.BigIntegerField(blank=True, null=True,
                                           verbose_name='قیمت هر متر')

    totalPrice = models.BigIntegerField(blank=True, null=True,
                                        verbose_name='قیمت کل')

    address = models.TextField(blank=True, null=True, verbose_name='آدرس')

    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    location = models.CharField(max_length=200, blank=True, null=True, verbose_name='آدرس در نقشه')

    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False,
                                           verbose_name='تاریخ و زمان ایجاد آگهی')

    priority = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True, null=True,
        verbose_name='اولویت',
    )

    pic1 = models.ImageField(upload_to='lands', blank=True, null=True, verbose_name='عکس ۱')
    pic2 = models.ImageField(upload_to='lands', blank=True, null=True, verbose_name='عکس ۲')
    pic3 = models.ImageField(upload_to='lands', blank=True, null=True, verbose_name='عکس ۳')
    pic4 = models.ImageField(upload_to='lands', blank=True, null=True, verbose_name='عکس ۴')
    pic5 = models.ImageField(upload_to='lands', blank=True, null=True, verbose_name='عکس ۵')
    pic6 = models.ImageField(upload_to='lands', blank=True, null=True, verbose_name='عکس ۶')

    class Meta:
        db_table = 'Land'
        verbose_name = 'آگهی زمین'
        verbose_name_plural = 'آگهی زمین ها'

    def __str__(self):
        return self.title


class Villa(models.Model):

    fa_db_name = models.CharField(max_length=20, editable=False, default='ویلا', verbose_name='نام جدول (فارسی)')
    en_db_name = models.CharField(max_length=20, editable=False, default='Villa', verbose_name='نام جدول (انگلیسی)')

    title = models.CharField(max_length=200, verbose_name='عنوان')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')

    landSize = models.IntegerField(blank=True, null=True, verbose_name='متراژ زمین')

    buildingSize = models.IntegerField(blank=True, null=True, verbose_name='متراژ بنا')

    NumberOfRooms = models.IntegerField(blank=True, null=True, verbose_name='تعداد اتاق خواب')

    adaptive = models.BooleanField(default=False, verbose_name='آیا قیمت توافقی است ؟')

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True, verbose_name='واحد پول')

    PricePerMeter = models.BigIntegerField(blank=True, null=True,
                                           verbose_name='قیمت هر متر')

    totalPrice = models.BigIntegerField(blank=True, null=True,
                                        verbose_name='قیمت کل')

    prepayment = models.IntegerField(blank=True, null=True, verbose_name='پیش پرداخت')

    rent = models.IntegerField(blank=True, null=True, verbose_name='اجاره')

    address = models.TextField(blank=True, null=True, verbose_name='آدرس')

    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    location = models.CharField(max_length=200, blank=True, null=True, verbose_name='آدرس در نقشه')

    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False,
                                           verbose_name='تاریخ و زمان ایجاد آگهی')

    priority = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True, null=True,
        verbose_name='اولویت',
    )

    pic1 = models.ImageField(upload_to='villas', blank=True, null=True, verbose_name='عکس ۱')
    pic2 = models.ImageField(upload_to='villas', blank=True, null=True, verbose_name='عکس ۲')
    pic3 = models.ImageField(upload_to='villas', blank=True, null=True, verbose_name='عکس ۳')
    pic4 = models.ImageField(upload_to='villas', blank=True, null=True, verbose_name='عکس ۴')
    pic5 = models.ImageField(upload_to='villas', blank=True, null=True, verbose_name='عکس ۵')
    pic6 = models.ImageField(upload_to='villas', blank=True, null=True, verbose_name='عکس ۶')

    class Meta:
        db_table = 'Villa'
        verbose_name = 'آگهی ویلا'
        verbose_name_plural = 'آگهی ویلا ها'

    def __str__(self):
        return self.title


class Apartment(models.Model):

    fa_db_name = models.CharField(max_length=20, editable=False, default='آپارتمان', verbose_name='نام جدول (فارسی)')
    en_db_name = models.CharField(max_length=20, editable=False, default='Apartment', verbose_name='نام جدول (انگلیسی)')

    title = models.CharField(max_length=200, verbose_name='عنوان')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی')

    NumberOfRooms = models.IntegerField(blank=True, null=True, verbose_name='تعداد اتاق خواب')

    floor = models.IntegerField(blank=True, null=True, verbose_name='طبقه')

    size = models.IntegerField(blank=True, null=True, verbose_name='متراژ')

    have_Warehouse = models.BooleanField(blank=True, null=True, verbose_name='آیا انباری دارد ؟')

    have_parking = models.BooleanField(blank=True, null=True, verbose_name='آیا پارکینگ دارد ؟')

    have_balcony = models.BooleanField(blank=True, null=True, verbose_name='آیا بالکن دارد ؟')

    adaptive = models.BooleanField(default=False, verbose_name='آیا قیمت توافقی است ؟')

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True, verbose_name='واحد پول')

    PricePerMeter = models.BigIntegerField(blank=True, null=True,
                                           verbose_name='قیمت هر متر')

    totalPrice = models.BigIntegerField(blank=True, null=True,
                                        verbose_name='قیمت کل')

    address = models.TextField(blank=True, null=True, verbose_name='آدرس')

    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    location = models.CharField(max_length=200, blank=True, null=True, verbose_name='آدرس در نقشه')

    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False,
                                           verbose_name='تاریخ و زمان ایجاد آگهی')

    priority = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True, null=True,
        verbose_name='اولویت',
    )

    pic1 = models.ImageField(upload_to='apartments', blank=True, null=True, verbose_name='عکس ۱')
    pic2 = models.ImageField(upload_to='apartments', blank=True, null=True, verbose_name='عکس ۲')
    pic3 = models.ImageField(upload_to='apartments', blank=True, null=True, verbose_name='عکس ۳')
    pic4 = models.ImageField(upload_to='apartments', blank=True, null=True, verbose_name='عکس ۴')
    pic5 = models.ImageField(upload_to='apartments', blank=True, null=True, verbose_name='عکس ۵')
    pic6 = models.ImageField(upload_to='apartments', blank=True, null=True, verbose_name='عکس ۶')

    class Meta:
        db_table = 'Apartment'
        verbose_name = 'آگهی آپارتمان'
        verbose_name_plural = 'آگهی آپارتمان ها'

    def __str__(self):
        return self.title