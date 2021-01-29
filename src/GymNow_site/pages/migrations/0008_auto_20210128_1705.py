# Generated by Django 2.2.17 on 2021-01-28 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20210128_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Donegal', 'Donegal'), ('Dublin', 'Dublin'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], max_length=200, null=True)),
                ('business_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Business_Owner')),
            ],
        ),
        migrations.AddField(
            model_name='bookings',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Booking_Location'),
        ),
    ]
