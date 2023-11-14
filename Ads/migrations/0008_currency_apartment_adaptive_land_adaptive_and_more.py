# Generated by Django 4.2.7 on 2023-11-14 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0007_remove_apartment_db_name_remove_land_db_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=20, verbose_name='واحد پول')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='adaptive',
            field=models.BooleanField(default=False, verbose_name='آیا قیمت توافقی است ؟'),
        ),
        migrations.AddField(
            model_name='land',
            name='adaptive',
            field=models.BooleanField(default=False, verbose_name='آیا قیمت توافقی است ؟'),
        ),
        migrations.AddField(
            model_name='villa',
            name='adaptive',
            field=models.BooleanField(default=False, verbose_name='آیا قیمت توافقی است ؟'),
        ),
        migrations.AddField(
            model_name='villa',
            name='prepayment',
            field=models.IntegerField(blank=True, null=True, verbose_name='پیش پرداخت'),
        ),
        migrations.AddField(
            model_name='villa',
            name='rent',
            field=models.IntegerField(blank=True, null=True, verbose_name='اجاره'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ads.currency', verbose_name='واحد پول'),
        ),
        migrations.AddField(
            model_name='land',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ads.currency', verbose_name='واحد پول'),
        ),
        migrations.AddField(
            model_name='villa',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ads.currency', verbose_name='واحد پول'),
        ),
    ]
