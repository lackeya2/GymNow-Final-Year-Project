# Generated by Django 2.2.17 on 2021-02-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210209_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business_owner',
            name='available_bookings',
        ),
        migrations.RemoveField(
            model_name='business_owner',
            name='price',
        ),
        migrations.CreateModel(
            name='Available_Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_bookings', models.ManyToManyField(to='pages.Bookings')),
            ],
        ),
    ]
