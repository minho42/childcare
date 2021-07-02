release: python manage.py migrate
web: gunicorn childcareapp.wsgi
celeryworker: celery -A childcareapp worker --beat --scheduler django --loglevel=info
