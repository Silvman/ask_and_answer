from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ask.models import Question, Answer, Tag
# Create your views here.

is_logged_in = 0


# def paginate(objects_list, request):
#
#     return objects_page, paginator

def pagination(list_item, page):
    paginator = Paginator(list_item, 10)
    try:
        return paginator.page(page), paginator
    except PageNotAnInteger:
        raise Http404("Page not an integer")
    except EmptyPage:
        return paginator.page(paginator.num_pages), paginator


def index(request, page_num=1):
    data, paginator = pagination(Question.objects.new().all(), page_num)
    context = {
        'view_name': 'question_list',
        'is_login': is_logged_in,
        'list_questions': data,
    }

    return render(request, 'index.html', context)

def hot(request, page_num=1):
    data, paginator = pagination(Question.objects.hot().all(), page_num)
    context = {
        'view_name': 'hot_list',
        'is_login': is_logged_in,
        'list_questions': data,
    }

    return render(request, 'index.html', context)


def question(request, question_id=0):
    list_answers = Answer.objects.all().filter(question_id = question_id)
    current_question = Question.objects.get(pk=question_id)
    context = {
        'is_login': is_logged_in,
        'list_answers': list_answers,
        'count': len(list_answers),
        'question': current_question,
    }
    return render(request, 'question.html', context)


def ask(request):
    context = {
        'is_login': is_logged_in,
        'lorem': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore '''
    }
    return render(request, 'ask.html', context)


def login(request):
    context = {
        'is_login': is_logged_in,
    }
    return render(request, 'login.html', context)


def signup(request):
    context = {
        'is_login': is_logged_in,
    }
    return render(request, 'signup.html', context)


def tag(request, tag_name="", page_num=1):
    if tag_name is "":
        raise Http404("Тэг не может быть пустым")

    try:
        tag = Tag.objects.get(title=tag_name)
    except Tag.DoesNotExist:
        raise Http404("Такого тега не существует")

    list_questions = tag.question_set.all()

    context = {
        'view_name': "tag_list",
        'tag_name': tag_name,
        'is_login': is_logged_in,
        'list_questions': list_questions,
    }

    return render(request, 'tag.html', context)


def settings(request):
    context = {
        'is_login': is_logged_in,
    }
    return render(request, 'settings.html', context)

def profile(request):
    raise Http404("Under construction")