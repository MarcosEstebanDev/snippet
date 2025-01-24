"""
WSGI config for django_snippets project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""


import os
import sys

path = '/home/MarcosEsDev/snippet'  # Ruta a tu proyecto
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'snippet.settings'  # Cambia 'snippet' por el nombre de tu proyecto

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()