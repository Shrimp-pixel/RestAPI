import json

from django.core.management.base import BaseCommand
from django.conf import settings

from userapp.models import User


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r', encoding='UTF-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()

        for i in range(5):
            User.objects.create(username=f'django{i}', first_name=f'firstname{i}', last_name=f'last_name{i}',
                                email=f"newuser{i}@exampl.com")
