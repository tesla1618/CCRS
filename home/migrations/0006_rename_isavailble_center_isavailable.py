# Generated by Django 4.2.1 on 2023-05-07 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_center_isavailble_center_rent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='center',
            old_name='isAvailble',
            new_name='isAvailable',
        ),
    ]
