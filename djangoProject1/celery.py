import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')

app = Celery('djangoProject1')

# Load tasks from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'
