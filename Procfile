release: python manage.py migrate && python manage.py collectstatic
web: gunicorn project.wsgi
celeryworker: celery -A project worker --beat --scheduler django --loglevel=info
