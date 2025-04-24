import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')

app.conf.broker_url =os.getenv('CELERY_BROKER_URL')

app.conf.broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_acks_late = True  
app.conf.task_reject_on_worker_lost = True  

@app.task(bind=True)
def debug_tasks(self):
    print(f'task executada: {self.request!r}')
    