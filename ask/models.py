from django.db import models

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by('-count_likes')

    def new(self):
        return self.order_by('-create_date')

    def of_user(self, username):
        return self.get(answer__author=username)

class UserManager(models.Manager):
    def get_user(self, login):
        try:
            return self.get(login=login)
        except self.DoesNotExist:
            return None

# TODO нужен менеджер для тэгов и лайков

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True, verbose_name=u"Аватар")

    def get_link(self):
        return reverse('profile_page') + '?id=' + str(self.pk)


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок тега")

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Автор")

    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Дата создания вопроса")
    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    rating = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Тэги")
    objects = QuestionManager()

    count_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Answer(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name=u"Автор ответа")
    question = models.ForeignKey(Question, models.SET_NULL, null=True, verbose_name=u"Ответ на вопрос")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Дата создания вопроса")
    is_correct = models.BooleanField(default=False)

    text = models.TextField(verbose_name=u"Текст ответа")


class Like(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Кто лайкнул")
    is_like = models.BooleanField(default=True, verbose_name=u"Является ли лайком")  # значение по умолчанию мб?
    question = models.ForeignKey(Question, models.SET_NULL, null=True, verbose_name=u"Вопрос")

    class Meta:
        unique_together = (('author', 'question'),)  # гарантирует только один лайк от одного юзера

#
# class AnswerLike(Like):
#
#
# class QuestionLike(Like):
#     class Meta:
#         unique_together = (('author', 'question'),)  # гарантирует только один лайк от одного юзера

# Create your models here.
