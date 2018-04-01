# -*- coding: utf-8 -*-
import os
from .settings import *

# DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shoppinglist_django',
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'TEST': {'CHARSET': 'UTF8'}
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# TEMPLATE_DEBUG = DEBUG
TEMPLATES[0]['OPTIONS']['debug'] = True
