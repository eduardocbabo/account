# Generated by Django 5.1.2 on 2024-10-24 14:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0011_alter_company_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_register',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_situation',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
