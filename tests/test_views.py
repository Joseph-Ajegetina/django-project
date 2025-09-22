from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from webapp.models import Task

class TaskViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Cloud Lab Django App')
    
    def test_task_list_view(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
    
    def test_add_task(self):
        response = self.client.post('/add/', {
            'title': 'Test Task',
            'description': 'Test Description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='Test Task').exists())
    
    def test_task_creation_validation(self):
        response = self.client.post('/add/', {
            'title': '',  # Empty title should fail
            'description': 'Test Description'
        })
        # Should stay on the same page due to validation error
        self.assertEqual(response.status_code, 200)
