from .base import *


DEBUG = False

ADMINS = [
    ('admin', 'email@admin.com'),
]

ALLOWED_HOSTS = ['*']
INSTALLED_APPS += ['django.contrib.postgres']

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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True