# Generated by Django 4.2.1 on 2023-05-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_center_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
