# Generated by Django 2.2.7 on 2021-04-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_booking_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingitem',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
