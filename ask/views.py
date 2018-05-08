from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST

from ask.models import Question, Tag, User, Like
from ask.forms import UserForm, QuestionForm

# Create your views here.

is_logged_in = 1


# def paginate(objects_list, request):
#
#     return objects_page, paginator

def pagination(list_item, page):
    paginator = Paginator(list_item, 10)
    try:
        return paginator.page(page), paginator
    except PageNotAnInteger:
        raise Http404("Page number is not an integer")
    except EmptyPage:
        return paginator.page(paginator.num_pages), paginator


def index(request, page_num=1):
    # лекция про авторизацию

    # https для передачи данных в открыто видел
    # # хеши с солью
    # # капча
    #
    # # атаки пытаются украсть куки : сложный ключ сесии, привязать к IP, ограничить сессию по времени, HttpOnly, запрос пароля при критических действиях
    #
    # user = request.user # определено всегда
    # if user.is_authenticated():
    #     pass
    # else:
    #     pass
    # ###


    data, paginator = pagination(Question.objects.new(), page_num)
    context = {
        'view_name': 'question_list',
        'is_login': is_logged_in,
        'list_questions': data,
    }



    return render(request, 'index.html', context)


def hot(request, page_num=1):
    data, paginator = pagination(Question.objects.hot(), page_num)
    context = {
        'view_name': 'hot_list',
        'is_login': is_logged_in,
        'list_questions': data,
    }

    return render(request, 'index.html', context)


def question(request, question_id=0):
    current_question = Question.objects.get(pk=question_id)
    list_answers = current_question.answer_set.all()
    context = {
        'is_login': is_logged_in,
        'list_answers': list_answers,
        'question': current_question,
    }
    return render(request, 'question.html', context)


def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('signup_page', pk=post.pk)
    else:
        form = UserForm()

    context = {
        'is_login': is_logged_in,
        'form': form,
    }
    return render(request, 'login.html', context)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.save()
            return redirect('login_page')
    else:
        form = UserForm()

    context = {
        'is_login': is_logged_in,
        'form': form,
    }
    return render(request, 'signup.html', context)


def tag(request, tag_name="", page_num=1):
    if tag_name is "":
        raise Http404("Тэг не может быть пустым")

    try:
        current_tag = Tag.objects.get(title=tag_name)
    except Tag.DoesNotExist:
        raise Http404("Такого тега не существует")

    data, paginator = pagination(current_tag.question_set.all(), page_num)

    context = {
        'view_name': "tag_list",
        'tag_name': tag_name,
        'is_login': is_logged_in,
        'list_questions': data,
    }

    return render(request, 'tag.html', context)


def settings(request):
    context = {
        'is_login': is_logged_in,
    }
    return render(request, 'settings.html', context)


def profile(request):
    raise Http404("Under construction")


def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():  # плохой, потмоу что появляется cleaned_data - неявно меняет состояние элемента
            q = form.save(commit=None)
            form.save()
            return redirect('question', q.pk)

    else:
        form = QuestionForm()  # unbound form

    context = {
        'is_login': is_logged_in,
        'form': form,
    }
    return render(request, 'ask.html', context)

@require_POST
def like(request):
    try:
        question_id = int(request.POST.get('question_id'))
    except ValueError: # int() кидает Value Error
        return JsonResponse({'status': 'error'})

    author = User.objects.first()

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


# request.is_ajax() - узнать, передается ли по аяксу

# пишем свой декоратор для корректной обработки неавторищованности, позволяет вернуть json в нужном случае, в отличии от login_required, который редиректит
# def login_req_ajax(view):
#     def

# CORS (нужно указывать origin, чтобы обработчик аякса вызвался)
# Allow Origins
# Allow Credentials
# BP:
# не ставить * в ответе, а проверить домен по списку двоеренных

#comet: nginx + push-stream-module

# эш низкоурованенный!