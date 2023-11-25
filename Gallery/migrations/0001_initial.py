# Generated by Django 4.2.7 on 2023-11-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Gallery', verbose_name='عکس')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'عکس ها',
                'db_table': 'Gallery',
            },
        ),
    ]