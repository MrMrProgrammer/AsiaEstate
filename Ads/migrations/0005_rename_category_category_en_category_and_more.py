# Generated by Django 4.2.6 on 2023-10-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0004_apartment_category_villa_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='en_category',
        ),
        migrations.AddField(
            model_name='category',
            name='fa_category',
            field=models.CharField(default='exit', max_length=20),
            preserve_default=False,
        ),
    ]
