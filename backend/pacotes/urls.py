# backend/pacotes/urls.py (VERSÃO CORRIGIDA E COMPLETA)

from django.urls import path
from . import views

urlpatterns = [
    # --- NOVA ROTA DE BUSCA ADICIONADA ---
    path('api/search/', views.buscar_pacotes, name='buscar_pacotes'),
    # -------------------------------------

    path('api/destinos/', views.listar_destinos, name='listar_destinos'),
    path('api/destinos/<int:destino_id>/pacotes/', views.listar_pacotes_por_destino, name='listar_pacotes_por_destino'),
    
    path('api/pacotes/', views.listar_pacotes, name='listar_pacotes'),
    path('api/pacotes/<int:pacote_id>/', views.detalhe_pacote, name='detalhe_pacote'),
]