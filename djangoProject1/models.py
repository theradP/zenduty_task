from django.db import models
from datetime import datetime


class Task(models.Model):
    PRIORITIES = (
        (0, 'High'),
        (1, 'Medium'),
        (2, 'Low'),
    )

    STATUSES = (
        (0, 'To Do'),
        (1, 'In Progress'),
        (2, 'Completed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    owner_email = models.EmailField()
    creator_email = models.EmailField()
    priority = models.IntegerField(choices=PRIORITIES)
    status = models.IntegerField(choices=STATUSES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
