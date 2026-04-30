# main/settings/pa.py
from .base import *

# Demo aşamasında hataları görmek için True kalabilir, sonra False yaparsın
DEBUG = config('DEBUG', default=True, cast=bool)

# Kendi kullanıcı adınla değiştir:
ALLOWED_HOSTS = [
    'umit8114.pythonanywhere.com',
    'localhost',
    '127.0.0.1'
] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Statik dosyalar için PA'nın beklediği klasör
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Django 4.0+ için POST/PUT/DELETE isteklerinde zorunludur
CSRF_TRUSTED_ORIGINS = [
    'https://umit8114.pythonanywhere.com'
]

# Güvenlik ayarları (SQLite ile çakışmaması için basit tutuyoruz)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False