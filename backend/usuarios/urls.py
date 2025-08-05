# backend/usuarios/urls.py (VERSÃO COMPLETA E CORRIGIDA)

from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # A página principal do perfil
    path('minha-conta/', views.minha_conta_view, name='minha_conta'),
    
    # --- ROTA ADICIONADA NOVAMENTE ---
    # O link 'minhas_viagens' agora aponta para a mesma view de 'minha_conta'
    path('minhas-viagens/', views.minha_conta_view, name='minhas_viagens'),
]