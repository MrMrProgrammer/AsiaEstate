# Generated by Django 4.2.7 on 2023-11-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseConfig', '0002_footerdata_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footerdata',
            options={'verbose_name': 'فوتر', 'verbose_name_plural': 'تنظیمات فوتر'},
        ),
        migrations.AddField(
            model_name='footerdata',
            name='landlineـphone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
