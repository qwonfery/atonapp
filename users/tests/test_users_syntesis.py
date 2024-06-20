# tests/test_commands.py
from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class SynthesizeUserDataTestCase(TestCase):

    def setUp(self):
        # Очистка таблицы пользователей перед каждым тестом
        User.objects.all().delete()

    def test_command_creates_users(self):
        # Запуск команды
        call_command('users_syntesis')

        # Проверка, что количество созданных пользователей соответствует ожидаемому
        expected_user_count = 16  # 4 first_names * 4 second_names
        self.assertEqual(User.objects.count(), expected_user_count)

        # Проверка, что каждый пользователь имеет корректные данные
        for first_name in ['John', 'Paul', 'George', 'Ringo']:
            for second_name in ['Lennon', 'McCartney', 'Harrison', 'Starr']:
                username = f"{first_name}{second_name}"
                full_name = f"{first_name} {second_name} Bitlovich"
                user = User.objects.get(username=username)
                self.assertEqual(user.full_name, full_name)
                self.assertTrue(user.check_password('1'))