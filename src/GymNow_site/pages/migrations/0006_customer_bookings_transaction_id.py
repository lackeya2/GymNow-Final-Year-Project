# Generated by Django 2.2.17 on 2021-03-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_bookings_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_bookings',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
