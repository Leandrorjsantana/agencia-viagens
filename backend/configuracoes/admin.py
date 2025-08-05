# backend/configuracoes/admin.py (VERSÃO COMPLETA E CORRIGIDA)

from django.contrib import admin
from .models import SiteConfiguracao

@admin.register(SiteConfiguracao)
class SiteConfiguracaoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identidade Visual', {'fields': ('logotipo', 'telefone_televendas', 'whatsapp_numero')}),
        ('Textos do Site', {'fields': ('texto_explore_destinos',)}),
        ('Cores do Tema', {'fields': ('cor_primaria', 'cor_secundaria', 'cor_fundo_hero')}),
        ('SEO (Otimização para Google)', {'fields': ('seo_title', 'seo_description')}),
        ('Marketing (Scripts de Rastreamento)', {'fields': ('tracking_scripts_head', 'tracking_scripts_body')}),
        # --- NOVA SEÇÃO ADICIONADA ---
        ('Redes Sociais', {'fields': ('link_instagram', 'link_facebook', 'link_twitter')}),
    )

    def response_change(self, request, obj):
        from django.http import HttpResponseRedirect
        self.message_user(request, "As configurações foram salvas com sucesso.")
        return HttpResponseRedirect(request.path)
    def has_add_permission(self, request): return False
    def has_delete_permission(self, request, obj=None): return False