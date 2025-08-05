# backend/usuarios/forms.py (VERSÃO COMPLETA E CORRIGIDA)

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        # A LISTA DE CAMPOS CORRETA, SEM O CAMPO 'endereco'
        fields = ('nome', 'email', 'telefone', 'cep', 'rua', 'numero', 'bairro', 'cidade', 'estado')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionamos placeholders e a classe do Bootstrap a todos os campos
        placeholders = {
            'nome': 'Seu nome completo',
            'email': 'seu-email@exemplo.com',
            'telefone': '(21) 99999-8888',
            'cep': 'Apenas números',
            'rua': 'Sua rua ou avenida',
            'numero': 'Ex: 123 ou S/N',
            'bairro': 'Seu bairro',
            'cidade': 'Sua cidade',
            'estado': 'UF',
            'password1': 'Crie uma senha',
            'password2': 'Confirme sua senha',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field_name, '')
            })
            # Deixa o campo de estado menor
            if field_name == 'estado':
                field.widget.attrs.update({'maxlength': '2'})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Seu e-mail'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sua senha'})