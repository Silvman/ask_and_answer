from django.db import models

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by('-rating')

    def new(self):
        return self.order_by('-createDate')

class UserManager(models.Manager):
    def get_user(self, login):
        try:
            return self.get(login=login)
        except self.DoesNotExist:
            return None

class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name=u"Аватар")
    def getLink(self):
        return reverse('profile', args=[self.id])


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок тега")

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Автор")

    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    createDate = models.DateTimeField(default=datetime.now, verbose_name=u"Дата создания вопроса")
    isActive = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    rating = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Тэги")
    objects = QuestionManager()
    numAnswers = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createDate']


class Answer(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name=u"Автор ответа")
    question = models.ForeignKey(Question, models.SET_NULL, null=True, verbose_name=u"Ответ на вопрос")
    createDate = models.DateTimeField(default=datetime.now, verbose_name=u"Дата создания вопроса")

    text = models.TextField(verbose_name=u"Текст ответа")


class Like(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Кто лайкнул")
    isLike = models.BooleanField(default=True, verbose_name=u"Является ли лайком")  # значение по умолчанию мб?


class AnswerLike(Like):
    answer = models.ForeignKey(Answer, models.SET_NULL, null=True, verbose_name=u"Ответ")


class QuestionLike(Like):
    question = models.ForeignKey(Question, models.SET_NULL, null=True, verbose_name=u"Вопрос")


# Create your models here.
