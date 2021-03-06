# Generated by Django 2.2.17 on 2021-04-17 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20210418_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buisness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Donegal', 'Donegal'), ('Dublin', 'Dublin'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow'), ('London', 'London')], max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.RenameField(
            model_name='business_owner',
            old_name='Owners_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer_bookings',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Customer'),
        ),
    ]
