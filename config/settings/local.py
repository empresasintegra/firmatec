"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='SppX+BTNkUqWd2zAtIpgf3c5w0ExH1ELaL30QP+GBCPebtPzT9kSMmRT5Q5JXj2LIC5R3CgpF0y5fI6oJHEmtw')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost'])
ALLOWED_HOSTS += [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "192.168.0.201",
    "192.168.0.111",
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405

# django CROS
CORS_ORIGIN_WHITELIST = [
    "http://localhost:4200", # angular
]
