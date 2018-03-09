from django.shortcuts import render

# Create your views here.

is_logged_in = 0

def index(request):
    list_questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        'is_login': is_logged_in,
        'list_questions': list_questions,
    'test': 'фыр',
    'lorem': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore '''
    }
    return render(request, 'index.html', context)

def question(request):
    list_comments = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        'is_login': is_logged_in,
        'list_comments': list_comments,
        'count': len(list_comments) + 3,
    'test': 'фыр',
    'lorem': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore '''
    }
    return render(request, 'question.html', context)


def ask(request):
    list_comments = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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



def tag(request):
    list_questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    context = {
        'is_login': is_logged_in,
        'list_questions': list_questions,
    }
    return render(request, 'tag.html', context)

def settings(request):
    context = {
        'is_login': is_logged_in,
    }
    return render(request, 'settings.html', context)

