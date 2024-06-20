# your_app/management/commands/clients_syntesis.py
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Sintesyze Client table with test data'
    first_names = ['John', 'Paul', 'George', 'Ringo']
    second_names = ['Lennon', 'McCartney', 'Harrison', 'Starr']
    third_name = 'Bitlovich'

    def handle(self, *args, **kwargs):

        test_users = [
            {
                'full_name': f"{first_name} {second_name} {self.third_name}",
                'username': f"{first_name}{second_name}",
                'password': '1'
            } for first_name in self.first_names for second_name in self.second_names
        ]

        for user_data in test_users:
            User.objects.create_user(
                username=user_data["username"],
                password=user_data['password'],
                full_name=user_data['full_name']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the User table with test data'))
