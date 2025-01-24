"""
WSGI config for django_snippets project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""


import os
import sys

# Ruta a tu proyecto Django
path = '/home/MarcosEsDev/snippet'
if path not in sys.path:
    sys.path.append(path)

# Configura el módulo de settings de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'snippet.settings'  # Cambia 'snippet' por el nombre de tu proyecto

# Carga la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()