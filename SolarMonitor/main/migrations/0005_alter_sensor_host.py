# Generated by Django 5.1.1 on 2024-10-06 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_ip_location_inverter_host_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='host',
            field=models.CharField(max_length=100, validators=[django.core.validators.URLValidator]),
        ),
    ]
