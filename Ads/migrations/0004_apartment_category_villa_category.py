# Generated by Django 4.2.6 on 2023-10-05 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0003_alter_apartment_title_alter_land_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ads.category', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='villa',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ads.category', verbose_name='دسته بندی'),
        ),
    ]