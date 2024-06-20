# tests/test_views.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from clients.models import Client

User = get_user_model()


class ClientViewsTestCase(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            full_name='Test User'
        )
        self.client.login(username=self.username, password=self.password)

        self.client1 = Client.objects.create(
            account_number='123456',
            last_name='Doe',
            first_name='John',
            middle_name='A',
            date_of_birth=timezone.now().date(),
            inn='123456789012',
            responsible_person=self.user.full_name,
            status='inactive'
        )

        self.client2 = Client.objects.create(
            account_number='789012',
            last_name='Smith',
            first_name='Jane',
            middle_name='B',
            date_of_birth=timezone.now().date(),
            inn='987654321098',
            responsible_person=self.user.full_name,
            status='inactive'
        )

    def test_client_list_view(self):
        # Тест GET-запроса к списку клиентов
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client_list.html')
        self.assertContains(response, self.client1.first_name)
        self.assertContains(response, self.client2.first_name)

    def test_update_client_status_view_success(self):
        # Тест успешного обновления статуса клиента
        response = self.client.post(reverse('update_client_status', args=[self.client1.id]), {
            'status': 'active',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'success'})
        self.client1.refresh_from_db()
        self.assertEqual(self.client1.status, 'active')



