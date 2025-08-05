# backend/usuarios/views.py (VERSÃO COMPLETA E CORRIGIDA)

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from pacotes.models import Reserva # Importamos o modelo Reserva

def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            send_mail('Bem-vindo à Sua Viagem!', f'Olá {user.nome},\n\nSeu cadastro foi realizado com sucesso!', 'nao-responda@suaagencia.com', [user.email])
            return redirect('usuarios:minha_conta')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuarios:minha_conta')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('pacotes:home')

@login_required
def minha_conta_view(request):
    # Busca todas as reservas do usuário que está logado, ordenando pelas mais recentes
    reservas = Reserva.objects.filter(usuario=request.user).order_by('-data_solicitacao')
    
    # Prepara o contexto para enviar os dados para o HTML
    contexto = {
        'reservas': reservas
    }
    return render(request, 'usuarios/minha_conta.html', contexto)