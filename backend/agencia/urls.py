from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Painel da Sua Viagem"
admin.site.site_title = "Administração | Sua Viagem"
admin.site.index_title = "Bem-vindo ao Painel de Controle"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pacotes.urls')),
    path('', include('configuracoes.urls')), # <-- Adicionamos a URL do novo app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)