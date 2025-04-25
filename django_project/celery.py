import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

BROKER_URL = os.getenv("RABBITMQ_URL")

app = Celery('django_project', broker=BROKER_URL)

app.conf.update(
    broker_connection_retry_on_startup=True,
)

app.conf.task_always_eager = False

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True, ignore_result=True)
def debug_tasks(self):
    print(f'task executada: {self.request!r}')
    