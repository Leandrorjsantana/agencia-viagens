# backend/pacotes/urls.py (VERSÃO CORRIGIDA E COMPLETA)

from django.urls import path
from . import views

app_name = 'pacotes'

urlpatterns = [
    # URLs das PÁGINAS
    path('', views.home_view, name='home'),
    path('destinos/<int:destino_id>/', views.destino_pacotes_view, name='destino_pacotes'),
    path('pacotes/<int:pacote_id>/', views.detalhe_pacote_view, name='detalhe_pacote_pagina'),
    path('busca/', views.pagina_busca_view, name='pagina_busca'),
    path('servicos/<str:categoria_slug>/', views.servico_categoria_view, name='servico_categoria'),
    path('servicos/item/<int:servico_id>/', views.servico_detalhe_view, name='servico_detalhe'),

    # URLs da API
    path('api/servicos/', views.api_listar_servicos, name='api_listar_servicos'),
    path('api/servicos/<str:categoria_slug>/', views.api_servicos_por_categoria, name='api_servicos_por_categoria'),
    path('api/servicos/item/<int:servico_id>/', views.api_detalhe_servico, name='api_detalhe_servico'),
    path('api/search/', views.buscar_pacotes, name='buscar_pacotes'),
    path('api/destinos/', views.listar_destinos, name='listar_destinos'), # <-- Rota restaurada
    path('api/destinos/<int:destino_id>/pacotes/', views.listar_pacotes_por_destino, name='listar_pacotes_por_destino'),
    path('api/solicitar-reserva/', views.solicitar_reserva, name='solicitar_reserva'),
    path('api/minhas-reservas/', views.api_listar_reservas, name='api_listar_reservas'),
    path('api/pacotes/<int:pacote_id>/', views.detalhe_pacote, name='detalhe_pacote_api'),
]