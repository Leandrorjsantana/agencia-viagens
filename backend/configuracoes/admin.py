from django.contrib import admin
from .models import SiteConfiguracao

@admin.register(SiteConfiguracao)
class SiteConfiguracaoAdmin(admin.ModelAdmin):
    # Proíbe que o administrador adicione novas configurações (só pode haver uma).
    def has_add_permission(self, request):
        return False
    # Proíbe que o administrador delete a configuração.
    def has_delete_permission(self, request, obj=None):
        return False