# Generated by Django 5.1.2 on 2024-10-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0007_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address_type',
            field=models.CharField(blank=True, choices=[('residential', 'Residencial'), ('commercial', 'Comercial')], default='residential', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='cep',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='cnpj',
            field=models.CharField(max_length=50),
        ),
    ]