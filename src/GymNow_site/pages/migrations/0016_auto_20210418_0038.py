# Generated by Django 2.2.17 on 2021-04-17 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20210418_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business_owner',
            old_name='Owner_name',
            new_name='name',
        ),
    ]