# Generated by Django 5.1.2 on 2024-10-23 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_remove_customuser_cpf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]