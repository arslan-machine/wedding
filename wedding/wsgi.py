"""
WSGI config for wedding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u1579453/data/www/wedding/wedding')
sys.path.insert(1, '/var/www/u1579453/data/djangoenv/lib/python3.9/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding.settings')

application = get_wsgi_application()
