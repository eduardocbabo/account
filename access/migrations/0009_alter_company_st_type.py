# Generated by Django 5.1.2 on 2024-10-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0008_alter_company_address_type_alter_company_cep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='st_type',
            field=models.CharField(blank=True, choices=[('av', 'Avenida'), ('st', 'Rua'), ('pl', 'Praca'), ('other', 'Outros')], default='st', max_length=20, null=True),
        ),
    ]