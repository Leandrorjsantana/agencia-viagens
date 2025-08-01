from django.db import models

class SiteConfiguracao(models.Model):
    logotipo = models.ImageField(upload_to='logos/', help_text="O logotipo que aparecerá no cabeçalho.")
    telefone_televendas = models.CharField(max_length=20, blank=True, help_text="Ex: 0800 123 4567")

    def __str__(self):
        return "Configurações Gerais do Site"

    # Este código garante que só possamos ter UMA instância deste modelo.
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteConfiguracao, self).save(*args, **kwargs)

    @classmethod
    def carregar(cls):
        # Este método prático nos ajuda a pegar a única instância de configuração.
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name_plural = "Configuração do Site"