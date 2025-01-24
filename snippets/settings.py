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

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # or 'bootstrap5' if you are using Bootstrap 5

# ...existing code...
