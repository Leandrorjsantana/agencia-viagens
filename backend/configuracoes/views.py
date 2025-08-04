from django.http import JsonResponse
from .models import SiteConfiguracao

def get_site_configuracao(request):
    config = SiteConfiguracao.carregar()
    data = {
        'logotipo_url': request.build_absolute_uri(config.logotipo.url) if config.logotipo else '',
        'telefone_televendas': config.telefone_televendas,
        'whatsapp_numero': config.whatsapp_numero, # <-- Novo campo
    }
    return JsonResponse(data)