
from django.templatetags.static import static
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError, RegexValidator,EmailValidator
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=50, null=False, blank=False)
    cnpj = models.CharField(
        max_length=14,
        validators=[RegexValidator(regex='^\d{14}$', message='O CNPJ deve ter 14 dígitos')],
        unique=True,
        null=False, 
        blank=False  
    )
    is_active = models.BooleanField(default=True)
    # user_supervised = models.ManyToManyField(User)
    # user_master = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # COMPANYSTATUS_CHOICES = [
    #     ('producing', 'Produzindo'),
    #     ('not_producing', 'Não produzindo'),
    # ]

    # status = models.CharField(
    #     max_length=20,
    #     choices=COMPANYSTATUS_CHOICES,
    #     default='ativo'
    # )
    cep = models.CharField(max_length=10, default='', blank=True, null=True)  # Formato: 00000-000
    address_type = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        choices=[('residential', 'Residencial'), ('commercial', 'Comercial')],
        default='commercial'
    )
    st_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=[('av', 'Avenida'), ('st', 'Rua'), ('pl', 'Praca'), ('other', 'Outros')],
        default='st'
    )
    address = models.CharField(max_length=255, default='', blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    UF_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=True, null=True)
    date_register = models.DateTimeField(default=timezone.now)
    date_last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    cpf = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex='^\d{11}$', message='O CPF deve ter 11 dígitos')],
        unique=True,
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    mobile = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^\d{10,11}$', message='Formato esperado: DD XXXXXXXXX')],
        blank=True,
        null=True
    )
    # ACCESS_CHOICES = [
    #     ('sales', 'Vendas'),
    #     ('master', 'Master'),
    # ]
    # access_type = models.CharField(max_length=30, choices=ACCESS_CHOICES, null=True, blank=True) #, default='sales')
    SITUATION_CHOICES = [
        ('liberado', 'Liberado'),
        ('andamento', 'Aguardando cadastro'),
        ('reprovado', 'Reprovado'),
        ('pendente', 'Pendente'),
    ]
    situation = models.CharField(max_length=30, choices=SITUATION_CHOICES, null=True, blank=True, default='andamento')
    # supervised_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True) # Empresa do usuário
    api = models.BooleanField(
        default=False,
        #verbose_name='Liberar API',
        help_text='Indica que este usuário tem as permissões para acessar API sem atribuí-las explicitamente.'    
    )
    bi = models.BooleanField(
        default=False,
        #verbose_name='Liberar acesso BI',
        help_text='Indica que este usuário tem as permissões para consumir dados do BI sem atribuí-las explicitamente.'    
    )
    info = models.TextField(null=True, blank=True)
    date_register = models.DateTimeField(default=timezone.now)
    date_situation = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    def get_profile_url(self):
        return reverse('profile', kwargs={'username': self.user.username})