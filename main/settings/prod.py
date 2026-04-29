# main/settings/prod.py
import dj_database_url
from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

# "*" yerine kendi adresinizi yazmak CSRF güvenliği için daha sağlıklıdır
ALLOWED_HOSTS = ["blog-api-product.up.railway.app", "localhost", "127.0.0.1"]

# Neon/Railway PostgreSQL ayarı
DATABASES = {
    'default': dj_database_url.config(
        # Değişken bulunamazsa sahte bir link kullan ki build çökmesin
        default=config("DATABASE_URL", default="postgres://user:pass@localhost:5432/db_name"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Statik Dosya Sunumu (WhiteNoise)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Güvenlik (HTTPS/CSRF)
CSRF_TRUSTED_ORIGINS = [
    "https://blog-api-product.up.railway.app",
    "https://*.up.railway.app",  # Railway'in tüm alt alan adlarına güven
    "https://*.railway.app",
]

# 1. Django'ya Railway proxy'sine güvenmesini söyleyin
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# 2. HTTPS Zorunluluğu
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Çerezlerin 'Lax' olması admin paneli için en uyumlusudur
    SESSION_COOKIE_SAMESITE = 'Lax'
    CSRF_COOKIE_SAMESITE = 'Lax'

CORS_ALLOWED_ORIGINS = [
    "blog-api-product.up.railway.app",
    ".up.railway.app",  # Tüm Railway subdomainleri
    "localhost",
    "127.0.0.1",
]