# Generated by Django 4.2.6 on 2023-10-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0002_category_alter_apartment_pricepermeter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='title',
            field=models.CharField(default='null', max_length=200, verbose_name='عنوان'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='land',
            name='title',
            field=models.CharField(default='Null', max_length=200, verbose_name='عنوان'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='villa',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
    ]
