# backend/usuarios/urls.py

from django.urls import path
from . import views

# Damos um "nome de aplicativo" para evitar conflitos de nomes de URL com outros apps
app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('minha-conta/', views.minha_conta_view, name='minha_conta'),
]