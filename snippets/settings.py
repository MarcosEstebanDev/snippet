# ...existing code...

DEBUG = False

# ...existing code...

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ...existing code...

INSTALLED_APPS = [
    # ...existing code...
    'crispy_forms',
    'crispy_bootstrap4',  # Add this if you are using Bootstrap 4
    # ...existing code...
]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'web-production-775a.up.railway.app']


CRISPY_TEMPLATE_PACK = 'bootstrap4'  # or 'bootstrap5' if you are using Bootstrap 5

STATIC_URL = '/static/'
STATIC_ROOT = '/home/MarcosEsDev/snippet/static'  # Ruta donde se recopilarán los archivos estáticos

# ...existing code...
