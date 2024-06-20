from django.core.management.base import BaseCommand
from clients.models import Client
from users.models import User
from datetime import date
import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.all()

        test_clients = [
            {
                "account_number": f"{user.pk}{i}",
                "last_name": "last",
                "first_name": "first",
                "middle_name": "middle",
                "date_of_birth": date(1980 + i % 20, 1 + i % 12, 1 + i % 28),
                "inn": f"{random.randint(100000000000, 999999999999)}",
                "responsible_person": user.full_name,
                "status": "inactive"
            } for i in range(1, random.randint(1, 5)) for user in users
        ]

        for client_data in test_clients:
            Client.objects.create(**client_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the Client table with test data'))
