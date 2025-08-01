# backend/pacotes/admin.py
from django.contrib import admin
from .models import Destino, Pacote, Avaliacao # Importamos nossos modelos

# O decorator @admin.register é a forma moderna de registrar um modelo.
@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    # Mostra essas colunas na lista de destinos
    list_display = ('nome',)
    # Adiciona uma barra de pesquisa que busca pelo nome
    search_fields = ('nome',)

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    # Mostra essas colunas na lista de pacotes
    list_display = ('nome', 'destino', 'preco', 'data_ida', 'disponivel')
    # Adiciona um filtro na lateral direita
    list_filter = ('disponivel', 'destino')
    # Adiciona uma barra de pesquisa
    search_fields = ('nome', 'destino__nome')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('pacote', 'nome_cliente', 'nota', 'data_avaliacao')
    list_filter = ('nota', 'pacote')
    search_fields = ('pacote__nome', 'nome_cliente')