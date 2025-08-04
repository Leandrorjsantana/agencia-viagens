# backend/pacotes/admin.py

from django.contrib import admin
from .models import Pacote, Destino

admin.site.register(Pacote)
admin.site.register(Destino)