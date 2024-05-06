from .base import *


DEBUG = False

ADMINS = [
    ('admin', 'email@admin.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('POSTGRES_DB'),
       'USER': config('POSTGRES_USER'),
       'PASSWORD': config('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True