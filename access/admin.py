from django.contrib import admin
from .models import Company, Profile
# from unfold.admin import ModelAdmin, StackedInline
from django.contrib.auth.models import User, Group
# from django.contrib.sites.models import Site
# from import_export.admin import ImportExportModelAdmin
# from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _
# from import_export.forms import ImportForm, ExportForm
from django.utils.html import format_html  # Necessário para renderizar HTML seguro
from django.urls import reverse
from django.contrib.auth import get_user_model

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj',)
    # import_form_class = ImportForm
    # export_form_class = ExportForm
    # export_form_class = SelectableFieldsExportForm
    filter_horizontal = ('user_supervised',)
    fieldsets = (
        (None, {
            'fields': ('name', 'razao_social', 'cnpj', 'user_master', 'user_supervised', 'status', 'is_active',)
        }),
        ('Endereço', {
            'fields': ('cep', 'address_type', 'st_type', 'address', 'number', 'complement', 'neighborhood', 'city', 'uf', ) 
        })
    )
admin.site.register(Company, CompanyAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'user__username', 'first_name', 'last_name', 'user__email', 'situation')
    search_fields = ('id', 'cpf', 'user__username', 'user__email')
    raw_id_fields = ('user',)
    # import_form_class = ImportForm
    # export_form_class = ExportForm
admin.site.register(Profile, ProfileAdmin)