from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command('users_syntesis')
        call_command('clients_syntesis')