from .base import *
import dj_database_url
import os

DEBUG = False

ALLOWED_HOSTS = [    
    "18.132.213.255",# your EC2 public IP
    "your-domain.com",
    "localhost",# optional for local dev
    "127.0.0.1",]


# Default to SQLite if DATABASE_URL not provided
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{Path(BASE_DIR) / 'db.sqlite3'}"
    )
}

# Redis
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/1")

# Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
