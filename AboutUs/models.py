from django.db import models


# Create your models here.

class AboutUs(models.Model):
    image = models.ImageField(upload_to='AboutUs', null=True, blank=True)

    header_1 = models.CharField(max_length=100, null=True, blank=True)
    body_1 = models.TextField(null=True, blank=True)

    header_2 = models.CharField(max_length=100, null=True, blank=True)
    body_2 = models.TextField(null=True, blank=True)

    header_3 = models.CharField(max_length=100, null=True, blank=True)
    body_3 = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'AboutUs'
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'