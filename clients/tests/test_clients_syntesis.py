# tests/test_commands.py
from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth import get_user_model
from clients.models import Client

User = get_user_model()


class SynthesizeClientDataTestCase(TestCase):

    def setUp(self):
        # Очистка таблицы пользователей и клиентов перед каждым тестом
        User.objects.all().delete()
        Client.objects.all().delete()

        # Создание тестовых пользователей
        self.users = [
            User.objects.create_user(
                username=f'user{i}',
                password='password',
                full_name=f'User {i} Test'
            ) for i in range(1, 6)
        ]

    def test_command_creates_clients(self):
        # Запуск команды
        call_command('clients_syntesis')

        # Проверка, что количество созданных клиентов соответствует ожидаемому диапазону
        clients = Client.objects.all()
        self.assertTrue(1 <= clients.count() <= len(self.users) * 4)

        # Проверка, что каждый клиент имеет корректные данные
        for client in clients:
            self.assertIn(client.responsible_person, [user.full_name for user in self.users])
            self.assertEqual(client.last_name, "last")
            self.assertEqual(client.first_name, "first")
            self.assertEqual(client.middle_name, "middle")
            self.assertEqual(client.status, "inactive")
            self.assertTrue(1980 <= client.date_of_birth.year <= 1999)
            self.assertTrue(1 <= client.date_of_birth.month <= 12)
            self.assertTrue(1 <= client.date_of_birth.day <= 28)
            self.assertTrue(100000000000 <= int(client.inn) <= 999999999999)