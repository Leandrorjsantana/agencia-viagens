# settings.py CORRIGIDO E COMPLETO

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-p3j5!rwuw!!r&k6&@g1*jvjp754i!2-hgr=6r&)=ka)(e846q#'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin', 'django.contrib.admin', 'django.contrib.auth',
    'django.contrib.contenttypes', 'django.contrib.sessions',
    'django.contrib.messages', 'django.contrib.staticfiles',
    'corsheaders', 'colorfield', 'pacotes', 'configuracoes', 
    'usuarios', 'paginas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agencia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR.parent, 'frontend')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'configuracoes.context_processors.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'agencia.wsgi.application'
AUTH_USER_MODEL = 'usuarios.Usuario'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR.parent, 'frontend'), os.path.join(BASE_DIR, 'static')]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CORS_ALLOW_ALL_ORIGINS = True

# --- CONFIGURAÇÕES DO JAZZMIN ATUALIZADAS ---
JAZZMIN_SETTINGS = {
    "site_title": "Admin Sua Viagem",
    "site_header": "Sua Viagem",
    "site_brand": "Painel Administrativo",
    "welcome_sign": "Bem-vindo ao painel de controle da Sua Viagem",
    "copyright": "Sua Viagem Ltda",
    
    # Dicionário de Ícones Completo
    "icons": {
        "auth": "fas fa-users-cog",
        "usuarios": "fas fa-users",
        "pacotes": "fas fa-suitcase-rolling",
        "configuracoes": "fas fa-cog",
        "paginas": "fas fa-file-alt",

        "auth.Group": "fas fa-users",
        "usuarios.Usuario": "fas fa-user",

        "pacotes.Destino": "fas fa-map-marked-alt",
        "pacotes.Pacote": "fas fa-box-open",
        "pacotes.Reserva": "fas fa-calendar-check",
        "pacotes.Servico": "fas fa-concierge-bell", # Ícone para o novo modelo
        
        "paginas.Pagina": "fas fa-file-invoice",
    },
    "show_ui_builder": False,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "brand_colour": "#341a6b",
    "accent": "#341a6b",
    "navbar": "navbar-white navbar-light",
    "sidebar": "sidebar-light-primary",
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "sidebar_nav_flat_style": True,
}