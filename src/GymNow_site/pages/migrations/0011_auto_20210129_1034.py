# Generated by Django 2.2.17 on 2021-01-29 10:34

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('pages', '0010_auto_20210128_1722'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking_Location',
            new_name='Location',
        ),
    ]