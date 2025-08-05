# backend/agencia/urls.py (VERSÃO COMPLETA E CORRIGIDA)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# As linhas de configuração do admin.site foram removidas daqui
# porque o Jazzmin e nosso template personalizado agora cuidam disso.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pacotes.urls')),
    path('', include('configuracoes.urls')),
    path('', include('usuarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)