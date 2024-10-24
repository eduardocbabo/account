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
# from django.contrib import admin
# from .models import Profile, Company
# from django.contrib import admin, messages
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError

# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'cnpj',)
#     search_fields = ('id', 'name', 'cnpj',)
#     # list_filter = ('id', 'name', 'cnpj',)
#     # import_form_class = ImportForm
#     # export_form_class = ExportForm
#     # export_form_class = SelectableFieldsExportForm
#     readonly_fields = ('date_register', 'date_last_update',) 
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'razao_social', 'cnpj', 'is_active',)
#         }),
#         ('Endereço', {
#             'fields': ('cep', 'address_type', 'st_type', 'address', 'number', 'complement', 'neighborhood', 'city', 'uf', ) 
#         }),
#         ('Registro', {
#             'fields': ('date_register', 'date_last_update',) 
#         }),
#     )
# admin.site.register(Company, CompanyAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cpf', 'user__username', 'first_name', 'last_name', 'user__email', 'situation')
#     search_fields = ('id', 'cpf', 'user__username', 'user__email')
#     raw_id_fields = ('user',)
#     # import_form_class = ImportForm
#     # export_form_class = ExportForm
#     readonly_fields = ('date_register', 'date_situation',) 
# admin.site.register(Profile, ProfileAdmin)


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].required = True  # Email obrigatório
#         self.fields['email'].label = _("Email") + " *"  # Rótulo com '*' para indicar obrigatoriedade

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email:
#             raise ValidationError(_("O campo e-mail é obrigatório."))

#         # Verifica se o email já existe
#         if User.objects.filter(email=email).exists():
#             raise ValidationError(_("Esse e-mail já está em uso."))
#         return email

# class UserAdmin(BaseUserAdmin):
#     add_form = CustomUserCreationForm  # Define o formulário customizado para adicionar usuários

#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')}),
#         (_('Permissions'), {'fields': ('groups',)}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
#         ),
#     )
#     readonly_fields = ('date_joined', 'last_login',)
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     ordering = ('username',)

#     def save_model(self, request, obj, form, change):
#         """Verificar se o e-mail está preenchido ao salvar."""
#         if not obj.email:
#             # Adiciona erro no formulário e mensagem na interface
#             form.add_error('email', "O campo e-mail é obrigatório.")
#             messages.error(request, "Não foi possível criar o usuário: o campo e-mail é obrigatório.")
#             return  # Impede o salvamento se houver erro

#         # Verifica se o username já existe
#         if User.objects.filter(username=obj.username).exists():
#             form.add_error('username', "Esse nome de usuário já está em uso.")
#             messages.error(request, "Não foi possível criar o usuário: o nome de usuário já está em uso.")
#             return  # Impede o salvamento se houver erro

#         super().save_model(request, obj, form, change)
# # Re-registra o modelo User com o UserAdmin customizado
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import Profile, Company
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class ActiveStatusFilter(admin.SimpleListFilter):
    title = 'Status Ativo'
    parameter_name = 'is_active'

    def lookups(self, request, model_admin):
        return (
            (True, 'Ativo'),
            (False, 'Inativo'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(is_active=True)
        if self.value() == 'False':
            return queryset.filter(is_active=False)
        return queryset

# class UFListFilter(admin.SimpleListFilter):
#     title = 'UF'
#     parameter_name = 'uf'

#     def lookups(self, request, model_admin):
#         # Usando as opções definidas em UF_CHOICES
#         return Company.UF_CHOICES

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(uf=self.value())
#         return queryset

def make_active(modeladmin, request, queryset):
    """Marcar as empresas selecionadas como ativas."""
    queryset.update(is_active=True)
    modeladmin.message_user(request, "Empresas selecionadas marcadas como ativas.")

def make_inactive(modeladmin, request, queryset):
    """Marcar as empresas selecionadas como inativas."""
    queryset.update(is_active=False)
    modeladmin.message_user(request, "Empresas selecionadas marcadas como inativas.")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'uf', 'is_active')
    search_fields = ('id', 'name', 'cnpj')
    list_filter = (ActiveStatusFilter,)  # Adiciona o filtro de status
    actions = [make_active, make_inactive]
    readonly_fields = ('date_register', 'date_last_update') 
    fieldsets = (
        (None, {
            'fields': ('name', 'razao_social', 'cnpj', 'is_active',)
        }),
        ('Endereço', {
            'fields': ('cep', 'address_type', 'st_type', 'address', 'number', 'complement', 'neighborhood', 'city', 'uf') 
        }),
        ('Registro', {
            'fields': ('date_register', 'date_last_update',) 
        }),
    )

admin.site.register(Company, CompanyAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'user__username', 'first_name', 'last_name', 'user__email', 'situation')
    search_fields = ('id', 'cpf', 'user__username', 'user__email')
    list_filter = (ActiveStatusFilter,)
    actions = [make_active, make_inactive]
    raw_id_fields = ('user',)
    readonly_fields = ('date_register', 'date_situation') 

admin.site.register(Profile, ProfileAdmin)

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
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    readonly_fields = ('date_joined', 'last_login',)
    actions = [make_active, make_inactive]
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

# Re-registra o modelo User com o UserAdmin customizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
