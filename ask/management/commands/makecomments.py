import random
import string

from django.core.management.base import BaseCommand, CommandError
from ask.models import Question, Answer


class Command(BaseCommand):
    help = u'Генерирует несколько комментов в указанный пост'

    def add_arguments(self, parser):
        parser.add_argument('q_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for question_id in options['q_id']:
            try:
                question = Question.objects.get(pk=question_id)
            except Question.DoesNotExist:
                raise CommandError(u'Вопроса "%s" не существует' % question_id)

            count = random.randint(1, 100)
            for i in range(count):
                answer = Answer(author_id=random.randint(1, 10), question_id=question_id, text=self.text_gen(100))
                answer.save()

            question.numAnswers = count
            question.save()

            self.stdout.write(self.style.SUCCESS('Накидали сообщений в псто "%s"' % question_id))

    @staticmethod
    def text_gen(size=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))
