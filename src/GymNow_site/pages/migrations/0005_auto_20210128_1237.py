# Generated by Django 2.2.17 on 2021-01-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210128_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='category',
            field=models.CharField(choices=[('Gym Booking', 'Gym Booking'), ('Personal Trainer', 'Personal Trainer'), ('Pilates', 'Pilates'), ('Yoga', 'Yoga'), ('Crossfit', 'Crossfit')], max_length=200, null=True),
        ),
    ]
