# Generated by Django 4.2.7 on 2023-12-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0002_alter_aboutus_body_1_alter_aboutus_body_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='body_1',
            field=models.TextField(blank=True, null=True, verbose_name='پاراگراف ۱'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='body_2',
            field=models.TextField(blank=True, null=True, verbose_name='پاراگراف ۲'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='body_3',
            field=models.TextField(blank=True, null=True, verbose_name='پاراگراف ۳'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='header_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان ۱'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='header_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان ۲'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='header_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان ۳'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='AboutUs', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]
