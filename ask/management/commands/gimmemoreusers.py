import string
import random
from django.core.management.base import BaseCommand
from ask.models import User


class Command(BaseCommand):
    help = u'Генерирует несколько рандомных сообщений'

    def handle(self, *args, **options):
        for i in range(10):
            user = User(username=self.text_gen(), password=self.text_gen(100) + "?")
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created user ' + user.username
                                                 + ' with pass' + user.password))

    @staticmethod
    def text_gen(size=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))
