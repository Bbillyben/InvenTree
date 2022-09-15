# Generated by Django 3.2.15 on 2022-09-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0086_remove_stockitem_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklocation',
            name='barcode_data',
            field=models.CharField(blank=True, help_text='Third party barcode data', max_length=500, verbose_name='Barcode Data'),
        ),
        migrations.AddField(
            model_name='stocklocation',
            name='barcode_hash',
            field=models.CharField(blank=True, help_text='Unique hash of barcode data', max_length=128, verbose_name='Barcode Hash'),
        ),
    ]
