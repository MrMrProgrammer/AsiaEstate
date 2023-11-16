# Generated by Django 4.2.7 on 2023-11-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GallerySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagination', models.IntegerField(default=9, verbose_name='تعداد عکس در هر صفحه')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'تنظیمات گالری',
                'verbose_name_plural': 'تنظیمات گالری',
                'db_table': 'GallerySetting',
            },
        ),
    ]
