# backend/pacotes/models.py (VERSÃO CORRIGIDA E COMPLETA)

from django.db import models

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem_padrao = models.ImageField(upload_to='destinos_imgs/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Pacote(models.Model):
    # --- NOVO CAMPO DE TIPO DE PACOTE ---
    TIPO_PACOTE_CHOICES = [
        ('DATA_FIXA', 'Data Fixa'),
        ('DATA_FLEXIVEL', 'Data Flexível (a combinar)'),
    ]
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_PACOTE_CHOICES,
        default='DATA_FIXA',
        help_text="Selecione se o pacote tem datas pré-definidas ou se as datas são flexíveis."
    )
    # ------------------------------------

    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao_curta = models.CharField(max_length=255)
    descricao_longa = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # --- CAMPOS DE DATA AGORA SÃO OPCIONAIS ---
    data_ida = models.DateField(null=True, blank=True, help_text="Obrigatório se o tipo for 'Data Fixa'.")
    data_volta = models.DateField(null=True, blank=True, help_text="Obrigatório se o tipo for 'Data Fixa'.")
    # ----------------------------------------
    
    disponivel = models.BooleanField(default=True)
    imagem_principal = models.ImageField(upload_to='pacotes_imgs/', null=True, blank=True)

    def __str__(self):
        return self.nome

# ... (Resto do arquivo com o modelo Avaliacao) ...
class Avaliacao(models.Model):
    pacote = models.ForeignKey(Pacote, related_name='avaliacoes', on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação de {self.nome_cliente} para {self.pacote.nome}'