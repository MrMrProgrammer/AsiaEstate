# Generated by Django 4.2.7 on 2023-11-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0011_apartment_prepayment_apartment_rent_land_prepayment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='prepayment',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='پیش پرداخت'),
        ),
        migrations.AlterField(
            model_name='land',
            name='rent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='اجاره'),
        ),
    ]