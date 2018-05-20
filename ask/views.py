from datetime import timedelta

from django.contrib.auth import authenticate, login, logout
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from ask.models import Question, Tag, User, Like, Answer
from ask.forms import SignupForm, QuestionForm, LoginForm, AnswerForm, ProfileEditForm

import json


# Create your views here.

def pagination(list_item, page):
    paginator = Paginator(list_item, 10)
    try:
        return paginator.page(page), paginator
    except PageNotAnInteger:
        return paginator.page(1), paginator
    except EmptyPage:
        return paginator.page(paginator.num_pages), paginator


def index(request):
    page_num = request.GET.get('page')
    data, paginator = pagination(Question.objects.new(), page_num)
    user = request.user
    context = {
        'view_name': 'question_list',
        'user': user,
        'list_questions': data,
    }

    return render(request, 'index.html', context)


def hot(request):
    page_num = request.GET.get('page')
    data, paginator = pagination(Question.objects.hot(), page_num)
    context = {
        'view_name': 'hot_list',
        'list_questions': data,
    }

    return render(request, 'index.html', context)


def question(request):
    try:
        question_id = int(request.GET.get('id'))
    except ValueError:
        raise Http404("id не число")

    current_question = Question.objects.get(pk=question_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:  # todo вернуть ошибку
            pass

        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = Answer.objects.create(author=request.user, question=current_question, text=form.cleaned_data['text'])
            return HttpResponseRedirect(request.get_full_path())
        else:  # todo вернуть ошибку
            pass
    else:
        form = AnswerForm()

    list_answers = current_question.answer_set.all()

    context = {
        'list_answers': list_answers,
        'question': current_question,
        'form': form,
    }
    return render(request, 'question.html', context)


def signin(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(form.cleaned_data['url'])

            else:
                error = u'Неверный логин\пароль'

    else:
        if request.GET.get('next'):
            form = LoginForm(initial={'url': request.GET.get('next')})
        else:
            form = LoginForm(initial={'url': '/'})

    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'login.html', context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data['username'],
                'a@a.a',
                form.cleaned_data['password'])
            return redirect('login_page')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def tag(request, tag_name=""):
    if tag_name is "":
        raise Http404("Тэг не может быть пустым")

    try:
        current_tag = Tag.objects.get(title=tag_name)
    except Tag.DoesNotExist:
        raise Http404("Такого тега не существует")

    page_num = request.GET.get('page')
    data, paginator = pagination(current_tag.question_set.all(), page_num)

    context = {
        'view_name': "tag_list",
        'tag_name': tag_name,
        'list_questions': data,
    }

    return render(request, 'tag.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():  # плохой, потмоу что появляется cleaned_data - неявно меняет состояние элемента
            if (request.user.username != form.cleaned_data['username']):
                #update


            return redirect(request.get_full_path())

    else:
        form = ProfileEditForm(initial=
                                {
                                    'username': request.user.username,
                                    'password': request.user.password,
                                    'avatar':   request.user.avatar,
                                    'email':    request.user.email,
                                })  # unbound form

    context = {
        'view_name': 'profile_page',
        'form': form,
    }

    return render(request, 'profile.html', context)


@login_required(login_url='/login/')
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():  # плохой, потмоу что появляется cleaned_data - неявно меняет состояние элемента
            q = form.save()
            q = Question.objects.get(pk=q.pk)
            q.author = request.user
            q.save()
            return redirect('/question/?id=' + str(q.pk))

    else:
        form = QuestionForm()  # unbound form

    context = {
        'form': form,
    }
    return render(request, 'ask.html', context)


def login_required_ajax(view):
    def decor_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        elif request.is_ajax():
            return JsonResponse(
                {
                    'status': 'error',
                    'message': u'Требуется авторизация',
                    'code': 'no_auth',
                }
            )
        else:
            redirect('/login/?continue=' + request.get_full_path())  # TODO хардкод

    return decor_view


@login_required_ajax
@require_POST
def like(request):
    try:
        question_id = int(request.POST.get('question_id'))
    except ValueError:  # int() кидает Value Error
        return JsonResponse({'status': 'error'})

    author = request.user

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return JsonResponse({'status': 'error'})

    # HttpResponseAjax(comment_id=id)
    # HttpResponseAjaxErrir(code="bad", message=form_errors.as_text)

    kwargs = {"author": author, "question": question}
    like_qs = Like.objects.filter(**kwargs)
    if like_qs.exists():
        like_qs.delete()
    else:
        Like.objects.create(**kwargs)

    question.count_likes = question.like_set.count()
    question.save()

    return JsonResponse({'status': 'ok', 'count': question.count_likes})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
