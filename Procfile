release: python manage.py migrate
web: gunicorn project.wsgi
celeryworker: celery -A project worker --beat --scheduler django --loglevel=info
