from django.db import models

class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Versão do título para a URL. Ex: seguro-viagem")
    conteudo = models.TextField(help_text="Use HTML para formatar o texto, se desejar.")
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
