# backend/pacotes/admin.py (VERSÃO COMPLETA E CORRIGIDA)

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Destino, Pacote, Reserva, Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    # --- LINHA CORRIGIDA AQUI ---
    list_display = ('nome', 'categoria', 'preco', 'disponivel')
    # ----------------------------
    list_filter = ('categoria', 'disponivel')
    search_fields = ('nome', 'descricao_curta')
    
    fieldsets = (
        ('Informações Principais', {
            'fields': ('categoria', 'nome', 'disponivel', 'imagem')
        }),
        ('Descrições', {
            'fields': ('descricao_curta', 'descricao_longa')
        }),
        ('Preço e Avaliação', {
            'fields': ('preco', 'taxas_inclusas', 'avaliacao')
        }),
        ('Detalhes Adicionais (Opcional)', {
            'classes': ('collapse',),
            'fields': ('cidade_origem', 'duracao_dias', 'duracao_noites')
        }),
        ('O que está incluso? (Opcional)', {
            'classes': ('collapse',),
            'fields': ('inclui_aereo', 'inclui_hotel', 'inclui_transfer')
        }),
    )

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'destino', 'preco', 'tipo', 'disponivel')
    list_filter = ('disponivel', 'tipo', 'destino')
    search_fields = ('nome', 'destino__nome')
    fieldsets = (
        ('Informações Principais', {'fields': ('nome', 'destino', 'disponivel', 'imagem_principal')}),
        ('Descrições', {'fields': ('descricao_curta', 'descricao_longa')}),
        ('Preço e Avaliação', {'fields': ('preco', 'taxas_inclusas', 'avaliacao')}),
        ('Detalhes da Viagem', {'fields': ('tipo', 'data_ida', 'data_volta', 'cidade_origem', 'duracao_dias', 'duracao_noites')}),
        ('O que está incluso?', {'fields': ('inclui_aereo', 'inclui_hotel', 'inclui_transfer')}),
    )

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('pacote', 'usuario', 'data_solicitacao', 'status', 'acoes_na_lista')
    list_filter = ('status', 'data_solicitacao')
    search_fields = ('pacote__nome', 'usuario__nome', 'usuario__email')
    readonly_fields = ('nome_cliente', 'email_cliente', 'telefone_cliente', 'data_solicitacao')
    actions = ['marcar_como_confirmada', 'marcar_como_cancelada']

    class Media:
        js = ('js/admin_reserva.js',)

    def marcar_como_confirmada(self, request, queryset):
        queryset.update(status='CONFIRMADA')
    marcar_como_confirmada.short_description = "Marcar selecionadas como Confirmadas"

    def marcar_como_cancelada(self, request, queryset):
        queryset.update(status='CANCELADA')
    marcar_como_cancelada.short_description = "Marcar selecionadas como Canceladas"

    def acoes_na_lista(self, obj):
        return format_html(
            '<a class="button" href="{}">Visualizar</a>&nbsp;',
            reverse('admin:pacotes_reserva_change', args=[obj.pk]),
        )
    acoes_na_lista.short_description = 'Ações'
    acoes_na_lista.allow_tags = True