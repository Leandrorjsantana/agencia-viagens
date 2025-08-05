# backend/configuracoes/models.py (VERSÃO COMPLETA E CORRIGIDA)

from django.db import models
from colorfield.fields import ColorField

class SiteConfiguracao(models.Model):
    # Campos existentes
    logotipo = models.ImageField(upload_to='logos/', help_text="O logotipo que aparecerá no cabeçalho e no painel de admin.")
    telefone_televendas = models.CharField(max_length=20, blank=True, help_text="Ex: 0800 123 4567")
    whatsapp_numero = models.CharField(max_length=20, blank=True, help_text="Número para o botão flutuante. Formato: 5511987654321")
    texto_explore_destinos = models.CharField(max_length=100, default='Explore nossos destinos', help_text="O título da seção de destinos na página inicial.")
    cor_primaria = ColorField(default='#341a6b', help_text="Cor principal do site (ex: #341a6b).")
    cor_secundaria = ColorField(default='#fd4f4f', help_text="Cor de destaque do site (ex: #fd4f4f).")
    cor_fundo_hero = ColorField(default='#fd7e14', help_text="Cor de fundo da seção de busca (o laranja).")
    seo_title = models.CharField("Título do Site (SEO)", max_length=70, blank=True, help_text="O título que aparece na aba do navegador e nos resultados do Google.")
    seo_description = models.CharField("Descrição do Site (SEO)", max_length=160, blank=True, help_text="Uma breve descrição do site para os resultados do Google.")
    tracking_scripts_head = models.TextField("Scripts no Cabeçalho (<head>)", blank=True, help_text="Cole aqui os scripts de rastreamento (Google Analytics, etc.).")
    tracking_scripts_body = models.TextField("Scripts no Corpo (<body>)", blank=True, help_text="Cole aqui os scripts (Google Tag Manager, etc.).")

    # --- NOVOS CAMPOS DE REDES SOCIAIS ---
    link_instagram = models.URLField("Link do Instagram", blank=True)
    link_facebook = models.URLField("Link do Facebook", blank=True)
    link_twitter = models.URLField("Link do Twitter / X", blank=True)
    # ------------------------------------
    
    def __str__(self): return "Configurações Gerais do Site"
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteConfiguracao, self).save(*args, **kwargs)
    @classmethod
    def carregar(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    class Meta:
        verbose_name_plural = "Configuração do Site"