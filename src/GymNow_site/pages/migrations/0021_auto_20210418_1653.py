# Generated by Django 2.2.17 on 2021-04-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20210418_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_bookings',
            name='order',
        ),
        migrations.AddField(
            model_name='customer_bookings',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]