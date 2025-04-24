web: gunicorn django_project.wsgi:application
worker: python -m celery -A django_project worker --loglevel=info