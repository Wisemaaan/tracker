from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_add_task(self):
        response = self.client.post(reverse('add_task'), {
            'title': 'Testing task',
            'description': 'Task description',
            'completed': False
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))

        tasks = Task.objects.filter(title='Testing task')
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks.first().user, self.user)


    def test_task_filtering(self):
    # Create two tasks: one completed, one not
        Task.objects.create(title='Completed Task', completed=True, user=self.user)
        Task.objects.create(title='Incomplete Task', completed=False, user=self.user)

        # Test 'completed' filter
        response = self.client.get(reverse('task_list') + '?filter=completed')
        self.assertContains(response, 'Completed Task')
        self.assertNotContains(response, 'Incomplete Task')

        # Test 'not_completed' filter
        response = self.client.get(reverse('task_list') + '?filter=not_completed')
        self.assertContains(response, 'Incomplete Task')
        self.assertNotContains(response, 'Completed Task')

        # Test 'all' filter
        response = self.client.get(reverse('task_list') + '?filter=all')
        self.assertContains(response, 'Completed Task')
        self.assertContains(response, 'Incomplete Task')
    





    def test_unauthenticated_access_redirect(self):
        self.client.logout()  # Ensure user is logged out

    # List of URLs that require login
        protected_urls = [
            reverse('task_list'),
            reverse('add_task'),
            reverse('edit_task', args=[1]),
            reverse('delete_task', args=[1]),
            reverse('toggle_task', args=[1]),
    ]

        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login/', response.url)