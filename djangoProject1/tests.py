from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_task_creation(self):
        response = self.client.post('/api/tasks/', {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'owner_email': 'owner@example.com',
            'creator_email': 'creator@example.com',
            'priority': 1,
            'status': 0,
        })
        self.assertEqual(response.status_code, 201)

        task = Task.objects.get(title='Test Task')
        self.assertEqual(task.description, 'This is a test task.')

    # Write more test cases for other API endpoints

    def test_celery_task(self):
        # Create a task with priority 0 and status 0
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            owner_email='owner@example.com',
            creator_email='creator@example.com',
            priority=0,
            status=0,
        )

        # Call the Celery task to update task statuses
        update_task_statuses()

        # Retrieve the updated task from the database
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.status, 1)

        # Call the Celery task again after 1 minute
        # Make sure to mock the current time to be 1 minute ahead
        update_task_statuses()

        # Retrieve the updated task from the database
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.status, 2)
