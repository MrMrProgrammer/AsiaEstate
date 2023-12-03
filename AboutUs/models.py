from django.db import models

class AboutUs(models.Model):
    image = models.ImageField(upload_to='AboutUs', null=True, blank=True, verbose_name='تصویر')

    header_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان ۱')
    body_1 = models.TextField(null=True, blank=True, verbose_name='پاراگراف ۱')

    header_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان ۲')
    body_2 = models.TextField(null=True, blank=True, verbose_name='پاراگراف ۲')

    header_3 = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان ۳')
    body_3 = models.TextField(null=True, blank=True, verbose_name='پاراگراف ۳')

    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        db_table = 'AboutUs'
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'