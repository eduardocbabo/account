# Generated by Django 5.1.2 on 2024-10-24 14:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0012_profile_date_register_profile_date_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='date_last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='date_register',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_situation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]