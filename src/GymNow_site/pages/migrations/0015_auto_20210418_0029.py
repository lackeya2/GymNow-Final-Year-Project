# Generated by Django 2.2.17 on 2021-04-17 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20210418_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business_owner',
            old_name='name',
            new_name='Owner_name',
        ),
    ]
