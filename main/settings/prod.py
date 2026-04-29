# main/settings/prod.py
import dj_database_url
from .base import *

DEBUG = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")

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
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]