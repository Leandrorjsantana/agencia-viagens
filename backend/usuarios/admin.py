# backend/usuarios/admin.py (VERSÃO COMPLETA E CORRIGIDA)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'nome', 'telefone', 'cidade', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'cidade', 'estado')
    search_fields = ('email', 'nome', 'cidade')
    ordering = ('email',)
    
    # Organiza o formulário de edição do usuário no admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'telefone')}),
        ('Endereço', {'fields': ('cep', 'rua', 'numero', 'bairro', 'cidade', 'estado')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )
    readonly_fields = ('last_login',)

admin.site.register(Usuario, CustomUserAdmin)