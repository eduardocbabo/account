# from django.contrib import admin
# from .models import Profile, Company
# from unfold.admin import ModelAdmin, StackedInline
# from django.contrib.auth.models import User, Group
# from django.contrib.sites.models import Site
# from import_export.admin import ImportExportModelAdmin
# from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
# from django.contrib.auth.admin import UserAdmin 
# from django.utils.translation import gettext_lazy as _
# from import_export.forms import ImportForm, ExportForm
# from django.utils.html import format_html  # Necessário para renderizar HTML seguro
# from django.urls import reverse
# from django.contrib.auth import get_user_model

# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'cnpj',)
#     # import_form_class = ImportForm
#     # export_form_class = ExportForm
#     # export_form_class = SelectableFieldsExportForm
#     filter_horizontal = ('user_supervised',)
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'razao_social', 'cnpj', 'user_master', 'user_supervised', 'status', 'is_active',)
#         }),
#         ('Endereço', {
#             'fields': ('cep', 'address_type', 'st_type', 'address', 'number', 'complement', 'neighborhood', 'city', 'uf', ) 
#         })
#     )
# admin.site.register(Company, CompanyAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cpf', 'user__username', 'first_name', 'last_name', 'user__email', 'situation')
#     search_fields = ('id', 'cpf', 'user__username', 'user__email')
#     raw_id_fields = ('user',)
#     # import_form_class = ImportForm
#     # export_form_class = ExportForm
# admin.site.register(Profile, ProfileAdmin)

# class CustomUserAdmin(UserAdmin):
#     list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)
#     # Exibe os campos na primeira tela (formulário de criação)
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_staff', 'is_superuser',),
#         }),
#     )

#     # Exibe os campos na tela de edição de usuário
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
#     )

# # Remove a versão padrão e registra a personalizada
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

# from django.contrib import admin
# from django.contrib.admin import AdminSite
# from .forms import CustomLoginForm
# from .models import CustomUser

# class CustomAdminSite(AdminSite):
#     login_form = CustomLoginForm  # Altera o formulário de login para o personalizado

# admin_site = CustomAdminSite(name='custom_admin')

# # Registre seu modelo CustomUser
# admin_site.register(CustomUser)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import CustomUser
# from django.contrib.auth import views as auth_views
# from .forms import CustomAuthenticationForm

# class CustomUserAdmin(BaseUserAdmin):
#     # Especifica quais campos serão exibidos na lista de usuários
#     list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser', 'is_email_verified', 'is_primary_email',)
    
#     # Define quais campos serão editáveis na página de detalhes do usuário
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password', 'is_email_verified', 'is_primary_email')}),
#         ('Informações pessoais', {'fields': ('first_name', 'last_name',)}),
#         ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Datas', {'fields': ('last_login',)}),
#     )
#     readonly_fields = ('is_email_verified', 'is_primary_email')
#     # Especifica quais campos podem ser editados na página de criação/edição
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_email_verified', 'is_primary_email')}
#         ),
#     )

#     # Define o campo que será usado para o login
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']  # ou outros campos que você deseja que sejam obrigatórios

# # Registre o modelo e o admin personalizado
# admin.site.register(CustomUser, CustomUserAdmin)

# class CustomAdminSite(admin.AdminSite):
#     login_form = CustomAuthenticationForm

# admin_site = CustomAdminSite(name='custom_admin')

from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True  # Email obrigatório
        self.fields['email'].label = _("Email") + " *"  # Rótulo com '*' para indicar obrigatoriedade

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError(_("O campo e-mail é obrigatório."))

        # Verifica se o email já existe
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Esse e-mail já está em uso."))

        return email


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm  # Define o formulário customizado para adicionar usuários

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')}),
        (_('Permissions'), {'fields': ('groups',)}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    readonly_fields = ('date_joined', 'last_login',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        """Verificar se o e-mail está preenchido ao salvar."""
        if not obj.email:
            # Adiciona erro no formulário e mensagem na interface
            form.add_error('email', "O campo e-mail é obrigatório.")
            messages.error(request, "Não foi possível criar o usuário: o campo e-mail é obrigatório.")
            return  # Impede o salvamento se houver erro

        # Verifica se o username já existe
        if User.objects.filter(username=obj.username).exists():
            form.add_error('username', "Esse nome de usuário já está em uso.")
            messages.error(request, "Não foi possível criar o usuário: o nome de usuário já está em uso.")
            return  # Impede o salvamento se houver erro

        super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        """Evita mensagens de sucesso desnecessárias ao adicionar um usuário."""
        if "_save" in request.POST and not obj.pk:
            # Se não houver ID do objeto (significa que não foi salvo), retorna ao formulário
            return self.add_view(request, form_url='', extra_context={'title': _('Add %s') % self.model._meta.verbose_name})

        return super().response_add(request, obj, post_url_continue)

# Re-registra o modelo User com o UserAdmin customizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
