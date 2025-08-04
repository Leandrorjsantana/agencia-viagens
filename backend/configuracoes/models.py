from django.db import models

class SiteConfiguracao(models.Model):
    logotipo = models.ImageField(upload_to='logos/', help_text="O logotipo que aparecerá no cabeçalho.")
    telefone_televendas = models.CharField(max_length=20, blank=True, help_text="Ex: 0800 123 4567")
    
    # --- NOVO CAMPO ADICIONADO ---
    whatsapp_numero = models.CharField(
        max_length=20, 
        blank=True, 
        help_text="Número para o botão flutuante. Formato: 5511987654321 (código do país + DDD + número)"
    )
    # -----------------------------

    def __str__(self):
        return "Configurações Gerais do Site"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteConfiguracao, self).save(*args, **kwargs)

    @classmethod
    def carregar(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name_plural = "Configuração do Site"