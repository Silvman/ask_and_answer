from django import forms
from django.core.exceptions import ValidationError

from ask.models import User, Question


class UserForm(forms.ModelForm):

    # 2й способ
    # описываем не в мете, указываем поля самостоятельно
    # # ничего не знаем о save, т.к. не знаем о модели
    # username = forms.CharField(max_length=11, min_length=5)
    # username1 = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'size': 40,
    #         'class': 'special',
    #         'qwe': 'asd'
    #     }
    # ))

    # валидация: сначала кастомная, затем clean

    # кастомная валидация поля username
    def clean_username(self):
        data = self.cleaned_data('username')
        if "*" in data:
            raise ValidationError("err")  # остальные эксепшны нельзя, будет ошибка на уровне сервера
        return data

    # валидация N полей
    # def clean(self):
    #     pass
    #
    class Meta:
        model = User
        fields = ('username', 'password')


class QuestionAdd(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('author', 'title', 'text')  # явно прописываем все?
