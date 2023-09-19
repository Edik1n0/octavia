release: python manage.py migrate
web: gunicorn octavia.wsgi --env DJANGO_SETTINGS_MODULE=octavia.settings