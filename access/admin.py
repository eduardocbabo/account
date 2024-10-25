from django.contrib import admin
from .models import Profile, Company
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from django.utils.html import format_html
from django.urls import reverse
from allauth.account.models import EmailAddress
from allauth.account.admin import EmailAddressAdmin as AllauthEmailAddressAdmin

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

class CompanyAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'uf', 'is_active')
    search_fields = ('id', 'name', 'cnpj')
    import_form_class = ImportForm
    export_form_class = ExportForm
    # export_form_class = SelectableFieldsExportForm
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

class GroupAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    import_form_class = ImportForm
    export_form_class = ExportForm
    # export_form_class = SelectableFieldsExportForm
    filter_horizontal = ('permissions',)
    fieldsets = (
        (None, {
            'fields': ('name', 'permissions',)
        }),
    )
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

class ProfileAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('id', 'cpf', 'user__username', 'first_name', 'last_name', 'email', 'company', 'situation')
    search_fields = ('id', 'cpf', 'user__username', 'email')
    import_form_class = ImportForm
    export_form_class = ExportForm
    # export_form_class = SelectableFieldsExportForm
    list_filter = (ActiveStatusFilter,)
    actions = [make_active, make_inactive]
    autocomplete_fields = ['user', 'company']  # Troca raw_id_fields por autocomplete_fields
    readonly_fields = ('date_register', 'date_situation')
#     # raw_id_fields = ('user',)

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



class UserAdmin(ModelAdmin, BaseUserAdmin, ImportExportModelAdmin):
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'password_reset_link',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')}),
        (_('Permissions'), {'fields': ('groups',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
        # (_('Password management'), {'fields': ('password_reset_link',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')},
        ),
    )
    readonly_fields = ('date_joined', 'last_login', 'password', 'password_reset_link')

    def password_reset_link(self, obj):
        """Cria um link com aparência de botão para redefinição de senha."""
        if obj.pk:  # Verifica se o usuário já existe
            url = reverse('admin:auth_user_password_change', args=[obj.pk])
            return format_html(
                '<div style="padding: 0; margin: 0; background: none; border: none;">'
                '<a href="{}" style="background-color: #2285ee; color: white; padding: 8px 16px; '
                'text-decoration: none; border-radius: 4px; font-weight: bold; display: inline-block; '
                'cursor: pointer;">'
                'Reset</a>'
                '</div>',
                url
            )
        return "Usuário ainda não foi salvo."
    
    password_reset_link.short_description = "Senha"

    list_display = (
        'username', 'email', 'first_name', 'last_name', 
        'is_active', 'is_staff', 'is_superuser', 'password_reset_link', 'email_button',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        if not obj.email:
            form.add_error('email', "O campo e-mail é obrigatório.")
            messages.error(request, "Não foi possível criar o usuário: o campo e-mail é obrigatório.")
            return  # Impede o salvamento

        if User.objects.filter(username=obj.username).exclude(pk=obj.pk).exists():
            form.add_error('username', "Esse nome de usuário já está em uso.")
            messages.error(request, "Não foi possível criar o usuário: o nome de usuário já está em uso.")
            return  # Impede o salvamento

        super().save_model(request, obj, form, change)

    def email_button(self, obj):
        if obj.pk:
            url = reverse('admin_send_email', args=[obj.pk])
            print(f"URL do botão de e-mail: {url}")  # Debug para ver a URL gerada
            return format_html(
        '<div style="padding: 0; margin: 0; background: none; border: none;">'
            '<a href="{}" style="background-color: #2285ee; color: white; padding: 8px 16px; '
            'text-decoration: none; border-radius: 4px; font-weight: bold; display: inline-block; '
            'cursor: pointer;">'
            'Enviar</a>'
            '</div>',
        url
    )

    email_button.short_description = 'Email'    

# Re-registrar o UserAdmin customizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(EmailAddress)

@admin.register(EmailAddress)
class EmailAddressAdmin(ModelAdmin, AllauthEmailAddressAdmin):
    list_display = ('email', 'user', 'verified', 'primary',)
    search_fields = ('email',)
    list_filter = ('verified', 'primary')

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
