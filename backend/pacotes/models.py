# backend/pacotes/models.py (VERSÃO COMPLETA E CORRIGIDA)

from django.db import models
from django.conf import settings

class Servico(models.Model):
    CATEGORIA_CHOICES = [
        ('OFERTA', 'Oferta Especial'), ('HOSPEDAGEM', 'Hospedagem'), ('PASSAGEM', 'Passagem Aérea'),
        ('CRUZEIRO', 'Cruzeiro'), ('SEGURO', 'Seguro Viagem'), ('DISNEY', 'Disney'),
        ('VISTO', 'Visto Consular'), ('CAMBIO', 'Câmbio'),
    ]

    categoria = models.CharField("Categoria", max_length=20, choices=CATEGORIA_CHOICES)
    nome = models.CharField(max_length=200, help_text="Ex: Hotel Copacabana Palace ou Seguro Viagem AC 35")
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField("Imagem Principal", upload_to='servicos/', null=True, blank=True)
    
    # --- CAMPOS AGORA SÃO OPCIONAIS ---
    descricao_curta = models.CharField(max_length=255, blank=True)
    descricao_longa = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço base", null=True, blank=True)
    taxas_inclusas = models.BooleanField(default=False, verbose_name="Taxas e impostos inclusos")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, help_text="Nota de 0.0 a 5.0")
    cidade_origem = models.CharField(max_length=100, blank=True, null=True, help_text="Ex: São Paulo (se aplicável)")
    duracao_dias = models.PositiveIntegerField(null=True, blank=True)
    duracao_noites = models.PositiveIntegerField(null=True, blank=True)
    inclui_aereo = models.BooleanField(default=False, verbose_name="Inclui Aéreo")
    inclui_hotel = models.BooleanField(default=False, verbose_name="Inclui Hotel")
    inclui_transfer = models.BooleanField(default=False, verbose_name="Inclui Transfer")
    # ------------------------------------

    def __str__(self):
        return f"{self.get_categoria_display()} - {self.nome}"

    class Meta:
        verbose_name = "Serviço Adicional"
        verbose_name_plural = "Serviços Adicionais"

# (O resto dos seus modelos - Destino, Pacote, Reserva - continuam aqui sem alterações)
class Destino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True, help_text="Uma breve descrição sobre o destino.")
    imagem_padrao = models.ImageField(upload_to='destinos_imgs/', null=True, blank=True)
    def __str__(self): return self.nome

class Pacote(models.Model):
    TIPO_PACOTE_CHOICES = [('DATA_FIXA', 'Data Fixa'), ('DATA_FLEXIVEL', 'Data Flexível (a combinar)')]
    nome = models.CharField(max_length=200, help_text="Ex: Pacotes para Rio de Janeiro")
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='pacotes')
    disponivel = models.BooleanField(default=True)
    imagem_principal = models.ImageField(upload_to='pacotes_imgs/', null=True, blank=True)
    descricao_curta = models.CharField(max_length=255)
    descricao_longa = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço base por pessoa.")
    taxas_inclusas = models.BooleanField(default=False, verbose_name="Taxas e impostos inclusos")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, help_text="Nota de 0.0 a 5.0")
    tipo = models.CharField(max_length=20, choices=TIPO_PACOTE_CHOICES, default='DATA_FLEXIVEL')
    data_ida = models.DateField(null=True, blank=True, help_text="Opcional se o tipo for 'Data Flexível'.")
    data_volta = models.DateField(null=True, blank=True, help_text="Opcional se o tipo for 'Data Flexível'.")
    cidade_origem = models.CharField(max_length=100, blank=True, null=True, help_text="Ex: São Paulo")
    duracao_dias = models.PositiveIntegerField(null=True, blank=True)
    duracao_noites = models.PositiveIntegerField(null=True, blank=True)
    inclui_aereo = models.BooleanField(default=False, verbose_name="Inclui Aéreo")
    inclui_hotel = models.BooleanField(default=False, verbose_name="Inclui Hotel")
    inclui_transfer = models.BooleanField(default=False, verbose_name="Inclui Transfer")
    def __str__(self): return self.nome

class Reserva(models.Model):
    STATUS_CHOICES = [('SOLICITADA', 'Solicitada'), ('CONFIRMADA', 'Confirmada'), ('CANCELADA', 'Cancelada')]
    pacote = models.ForeignKey(Pacote, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SOLICITADA')
    nome_cliente = models.CharField(max_length=150)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20)
    def __str__(self): return f'Reserva de {self.pacote.nome} para {self.usuario.nome}'