from django.db import models
import jdatetime
import pytz


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='')
    phone_number = models.CharField(max_length=20, verbose_name='')
    message = models.TextField(verbose_name='')
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='زمان ارسال پیام')

    def jalali_created_at(self):
        tz = pytz.timezone('Asia/Tehran')
        dt = self.created_at.astimezone(tz)
        j_date = jdatetime.datetime.fromgregorian(datetime=dt)
        return j_date.strftime('%d-%m-%Y  |  %H:%M')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ContactUs'
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'