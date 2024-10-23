
# from django.templatetags.static import static
# from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError, RegexValidator,EmailValidator
# from django.utils import timezone
# from django.urls import reverse
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class Company(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     razao_social = models.CharField(max_length=50, null=False, blank=False)
#     cnpj = models.CharField(max_length=50, null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     user_supervised = models.ManyToManyField(User)
#     user_master = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
#     COMPANYSTATUS_CHOICES = [
#         ('producing', 'Produzindo'),
#         ('not_producing', 'Não produzindo'),
#     ]

#     status = models.CharField(
#         max_length=20,
#         choices=COMPANYSTATUS_CHOICES,
#         default='ativo'
#     )
#     cep = models.CharField(max_length=10, default='')  # Formato: 00000-000
#     address_type = models.CharField(
#         max_length=15,
#         choices=[('residential', 'Residencial'), ('commercial', 'Comercial')],
#         default='residential'
#     )
#     st_type = models.CharField(
#         max_length=20,
#         choices=[('av', 'Avenida'), ('st', 'Rua'), ('pl', 'Praca'), ('other', 'Outros')],
#         default='st'
#     )
#     address = models.CharField(max_length=255, default='', blank=True, null=True)
#     number = models.CharField(max_length=10, blank=True, null=True)
#     complement = models.CharField(max_length=50, blank=True, null=True)
#     neighborhood = models.CharField(max_length=100, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     UF_CHOICES = [
#         ('AC', 'Acre'),
#         ('AL', 'Alagoas'),
#         ('AP', 'Amapá'),
#         ('AM', 'Amazonas'),
#         ('BA', 'Bahia'),
#         ('CE', 'Ceará'),
#         ('DF', 'Distrito Federal'),
#         ('ES', 'Espírito Santo'),
#         ('GO', 'Goiás'),
#         ('MA', 'Maranhão'),
#         ('MT', 'Mato Grosso'),
#         ('MS', 'Mato Grosso do Sul'),
#         ('MG', 'Minas Gerais'),
#         ('PA', 'Pará'),
#         ('PB', 'Paraíba'),
#         ('PR', 'Paraná'),
#         ('PE', 'Pernambuco'),
#         ('PI', 'Piauí'),
#         ('RJ', 'Rio de Janeiro'),
#         ('RN', 'Rio Grande do Norte'),
#         ('RS', 'Rio Grande do Sul'),
#         ('RO', 'Rondônia'),
#         ('RR', 'Roraima'),
#         ('SC', 'Santa Catarina'),
#         ('SP', 'São Paulo'),
#         ('SE', 'Sergipe'),
#         ('TO', 'Tocantins'),
#     ]
#     uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=True, null=True)

#     def __str__(self):
#         return self.name
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     cpf = models.CharField(
#         max_length=11,
#         validators=[RegexValidator(regex='^\d{11}$', message='O CPF deve ter 11 dígitos')],
#         unique=True,
#         blank=True,
#         null=True
#     )
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     email = models.EmailField(max_length=254, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     mobile = models.CharField(
#         max_length=11,
#         validators=[RegexValidator(regex=r'^\d{10,11}$', message='Formato esperado: DD XXXXXXXXX')],
#         blank=True,
#         null=True
#     )
#     # ACCESS_CHOICES = [
#     #     ('sales', 'Vendas'),
#     #     ('master', 'Master'),
#     # ]
#     # access_type = models.CharField(max_length=30, choices=ACCESS_CHOICES, null=True, blank=True) #, default='sales')
#     SITUATION_CHOICES = [
#         ('liberado', 'Liberado'),
#         ('andamento', 'Aguardando cadastro'),
#         ('reprovado', 'Reprovado'),
#         ('pendente', 'Pendente'),
#     ]
#     situation = models.CharField(max_length=30, choices=SITUATION_CHOICES, null=True, blank=True, default='andamento')
#     # supervised_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     # company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True) # Empresa do usuário
#     api = models.BooleanField(
#         default=False,
#         #verbose_name='Liberar API',
#         help_text='Indica que este usuário tem as permissões para acessar API sem atribuí-las explicitamente.'    
#     )
#     bi = models.BooleanField(
#         default=False,
#         #verbose_name='Liberar acesso BI',
#         help_text='Indica que este usuário tem as permissões para consumir dados do BI sem atribuí-las explicitamente.'    
#     )
#     info = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return str(self.user)
    
#     def get_profile_url(self):
#         return reverse('profile', kwargs={'username': self.user.username})
















# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     is_email_verified = models.BooleanField(default=False)
#     is_primary_email = models.BooleanField(default=False)
#     # cpf = models.CharField(
#     #     max_length=11,
#     #     validators=[RegexValidator(regex='^\d{11}$', message='O CPF deve ter 11 dígitos')],
#     #     unique=True,
#     #     blank=True,
#     #     null=True
#     # )

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']  # ou outros campos que você deseja que sejam obrigatórios

#     def __str__(self):
#         return self.email
    

# from django.contrib.auth.models import BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         """Cria e retorna um usuário com email e senha."""
#         if not email:
#             raise ValueError("O email deve ser fornecido.")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """Cria e retorna um superusuário com email e senha."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         # Certifique-se de que o superusuário tenha um username
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError("Superuser deve ter is_staff=True.")
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError("Superuser deve ter is_superuser=True.")

#         # Aqui você pode definir um username padrão, por exemplo, o email
#         username = email.split('@')[0]  # ou alguma outra lógica que você preferir
#         return self.create_user(email, password, username=username, **extra_fields)

