import string
import random
from django.core.management.base import BaseCommand
from ask.models import Question, User


class Command(BaseCommand):
    help = u'Генерирует несколько рандомных сообщений'

    def handle(self, *args, **options):
        for i in range(10):
            question = Question(title=self.text_gen(), text=self.text_gen(20) + " " + self.text_gen(20) + " " + self.text_gen(20) + "?",
                                author=User.objects.get(id=random.randint(1, 10)), rating=i)
            question.save()
            self.stdout.write(self.style.SUCCESS('Successfully created question ' + question.title
                                                 + ' with text ' + question.text))

    @staticmethod
    def text_gen(size=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))
