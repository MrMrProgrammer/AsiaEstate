from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='Gallery', verbose_name='عکس')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'Gallery'
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'
