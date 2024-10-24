# Generated by Django 5.1.2 on 2024-10-23 20:54

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access', '0005_delete_customuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('razao_social', models.CharField(max_length=50)),
                ('cnpj', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('cep', models.CharField(default='', max_length=10)),
                ('address_type', models.CharField(choices=[('residential', 'Residencial'), ('commercial', 'Comercial')], default='residential', max_length=15)),
                ('st_type', models.CharField(choices=[('av', 'Avenida'), ('st', 'Rua'), ('pl', 'Praca'), ('other', 'Outros')], default='st', max_length=20)),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('complement', models.CharField(blank=True, max_length=50, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='O CPF deve ter 11 dígitos', regex='^\\d{11}$')])),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='Formato esperado: DD XXXXXXXXX', regex='^\\d{10,11}$')])),
                ('situation', models.CharField(blank=True, choices=[('liberado', 'Liberado'), ('andamento', 'Aguardando cadastro'), ('reprovado', 'Reprovado'), ('pendente', 'Pendente')], default='andamento', max_length=30, null=True)),
                ('api', models.BooleanField(default=False, help_text='Indica que este usuário tem as permissões para acessar API sem atribuí-las explicitamente.')),
                ('bi', models.BooleanField(default=False, help_text='Indica que este usuário tem as permissões para consumir dados do BI sem atribuí-las explicitamente.')),
                ('info', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]