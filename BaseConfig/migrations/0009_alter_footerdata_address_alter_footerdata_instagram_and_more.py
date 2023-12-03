# Generated by Django 4.2.7 on 2023-12-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseConfig', '0008_alter_footerdata_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerdata',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='landline_phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن ثابت'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='موقعیت در نقشه'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='per_page_item',
            field=models.IntegerField(default=10, verbose_name='تعداد آگهی در هر صفحه'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='site_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات سایت'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to='footer/site_logo', verbose_name='لوگوسایت'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='telegram',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تلگرام'),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='واتس اپ'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='home_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات در صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(upload_to='Slider', verbose_name='تصویر اسلایدر'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]