# Generated by Django 2.2.17 on 2021-01-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_business_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Gym Booking', 'Gym Booking'), ('Personal Trainer', 'Personal Trainer'), ('Pilates', 'Pilates'), ('Yoga', 'Yoga')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]