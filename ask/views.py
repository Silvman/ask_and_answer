from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
# Create your views here.

is_logged_in = 0
paginator_count = 10

def index(request, page_num = 1, hot = 0):
    questions = []
    for i in range(1, 30):
        questions.append(
            {
                'view_name': 'question_list',
                'title': 'title ' + str(i),
                'id': i,
                'text': 'text' + str(i)
            }
        )

    paginator = Paginator(questions, paginator_count)
    if page_num < 1:
        page_num = 1

    try:
        list_questions = paginator.page(page_num)
    except EmptyPage:
        list_questions = paginator.page(paginator.num_pages)

    context = {
        'view_name': 'question_list',
        'is_login': is_logged_in,
        'list_questions': list_questions,
    }

    return render(request, 'index.html', context)

def question(request, question_id = 0):
    list_comments = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        'is_login': is_logged_in,
        'list_comments': list_comments,
        'count': len(list_comments),
    'test': 'фыр',
    'lorem': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore '''
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



def tag(request, tag_name= "", page_num=1):
    questions = []
    for i in range(1, 30):
        questions.append(
            {
                'title': 'title ' + str(i),
                'id': i,
                'text': 'text' + str(i)
            }
        )

    paginator = Paginator(questions, paginator_count)
    if page_num < 1:
        page_num = 1

    try:
        list_questions = paginator.page(page_num)
    except EmptyPage:
        list_questions = paginator.page(paginator.num_pages)



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

