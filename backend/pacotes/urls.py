# backend/pacotes/urls.py (VERSÃO CORRIGIDA E COMPLETA)

from django.urls import path
from . import views

app_name = 'pacotes'

urlpatterns = [
    # URLs das PÁGINAS
    path('', views.home_view, name='home'),
    path('destinos/<int:destino_id>/', views.destino_pacotes_view, name='destino_pacotes'),
    path('pacotes/<int:pacote_id>/', views.detalhe_pacote_view, name='detalhe_pacote_pagina'),
    # --- NOVA ROTA ADICIONADA PARA A PÁGINA DE BUSCA ---
    path('busca/', views.pagina_busca_view, name='pagina_busca'),
    # ----------------------------------------------------

    # URLs da API (não mudam)
    path('api/search/', views.buscar_pacotes, name='buscar_pacotes'),
    path('api/destinos/', views.listar_destinos, name='listar_destinos'),
    path('api/destinos/<int:destino_id>/pacotes/', views.listar_pacotes_por_destino, name='listar_pacotes_por_destino'),
    path('api/solicitar-reserva/', views.solicitar_reserva, name='solicitar_reserva'),
    path('api/pacotes/<int:pacote_id>/', views.detalhe_pacote, name='detalhe_pacote_api'),
]