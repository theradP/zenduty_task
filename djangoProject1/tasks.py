from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Task


@shared_task
def update_task_statuses():
    tasks = Task.objects.all()

    for task in tasks:
        if task.priority == 0:
            if (timezone.now() - task.created_at) >= timedelta(seconds=30):
                task.status = 1
                task.save()
            elif (timezone.now() - task.created_at) >= timedelta(minutes=1):
                task.status = 2
                task.save()
        elif task.priority == 1:
            if (timezone.now() - task.created_at) >= timedelta(minutes=1):
                task.status = 1
                task.save()
            elif (timezone.now() - task.created_at) >= timedelta(minutes=2):
                task.status = 2
                task.save()
        elif task.priority == 2:
            if (timezone.now() - task.created_at) >= timedelta(minutes=2):
                task.status = 1
                task.save()
            elif (timezone.now() - task.created_at) >= timedelta(minutes=5):
                task.status = 2
                task.save()
