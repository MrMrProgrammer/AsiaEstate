from django.db import models


# Create your models here.

class Logger(models.Model):
    date = models.CharField(max_length=20, verbose_name="تاریخ")
    time = models.CharField(max_length=20, verbose_name="زمان")
    ip = models.CharField(max_length=20, verbose_name="IP")
    agent = models.CharField(max_length=500, verbose_name="مرورگر")
    language = models.CharField(max_length=100, verbose_name="زبان")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = "بازدید ها"