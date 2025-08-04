from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Enviar e-mail de boas-vindas
            assunto = 'Bem-vindo à Sua Viagem!'
            mensagem = f'Olá {user.nome},\n\nSeu cadastro foi realizado com sucesso!\n\nExplore nossos destinos e planeje sua próxima aventura.'
            send_mail(assunto, mensagem, 'nao-responda@suaagencia.com', [user.email])

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
    # Lógica para a mensagem do WhatsApp
    numero_agencia = '5511999999999' # SEU NÚMERO
    mensagem_whats = f'Olá! Acabei de me cadastrar no site Sua Viagem. Meu nome é {request.user.nome} e meu e-mail é {request.user.email}.'
    link_whats = f'https://wa.me/{numero_agencia}?text={mensagem_whats}'
    
    contexto = {
        'link_whatsapp': link_whats
    }
    return render(request, 'usuarios/minha_conta.html', contexto)