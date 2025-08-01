from django.urls import path
from . import views

urlpatterns = [
    path('api/configuracao/', views.get_site_configuracao, name='get_site_configuracao'),
]