# backend/configuracoes/context_processors.py

from .models import SiteConfiguracao

def site_config(request):
    """
    Disponibiliza as configurações do site para todos os templates.
    """
    config = SiteConfiguracao.carregar()
    return {
        'site_config': config
    }