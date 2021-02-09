# Generated by Django 2.2.17 on 2021-02-09 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20210207_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_owner',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_price', to='pages.Bookings'),
        ),
        migrations.AlterField(
            model_name='business_owner',
            name='available_bookings',
            field=models.ManyToManyField(related_name='available_bookings', to='pages.Bookings'),
        ),
    ]
