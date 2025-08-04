# backend/pacotes/models.py (VERSÃO COMPLETA E CORRIGIDA)

from django.db import models

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True, help_text="Uma breve descrição sobre o destino.")
    imagem_padrao = models.ImageField(upload_to='destinos_imgs/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Pacote(models.Model):
    TIPO_PACOTE_CHOICES = [
        ('DATA_FIXA', 'Data Fixa'),
        ('DATA_FLEXIVEL', 'Data Flexível (a combinar)'),
    ]

    # Informações Principais
    nome = models.CharField(max_length=200, help_text="Ex: Pacotes para Rio de Janeiro")
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='pacotes')
    disponivel = models.BooleanField(default=True)
    imagem_principal = models.ImageField(upload_to='pacotes_imgs/', null=True, blank=True)

    # Descrições
    descricao_curta = models.CharField(max_length=255)
    descricao_longa = models.TextField()

    # Preço e Avaliação
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço base por pessoa.")
    taxas_inclusas = models.BooleanField(default=False, verbose_name="Taxas e impostos inclusos")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, help_text="Nota de 0.0 a 5.0")

    # Detalhes da Viagem
    tipo = models.CharField(max_length=20, choices=TIPO_PACOTE_CHOICES, default='DATA_FLEXIVEL')
    data_ida = models.DateField(null=True, blank=True, help_text="Opcional se o tipo for 'Data Flexível'.")
    data_volta = models.DateField(null=True, blank=True, help_text="Opcional se o tipo for 'Data Flexível'.")
    cidade_origem = models.CharField(max_length=100, blank=True, null=True, help_text="Ex: São Paulo")
    duracao_dias = models.PositiveIntegerField(null=True, blank=True)
    duracao_noites = models.PositiveIntegerField(null=True, blank=True)

    # O que inclui
    inclui_aereo = models.BooleanField(default=False, verbose_name="Inclui Aéreo")
    inclui_hotel = models.BooleanField(default=False, verbose_name="Inclui Hotel")
    inclui_transfer = models.BooleanField(default=False, verbose_name="Inclui Transfer")

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    pacote = models.ForeignKey(Pacote, related_name='avaliacoes', on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação de {self.nome_cliente} para {self.pacote.nome}'