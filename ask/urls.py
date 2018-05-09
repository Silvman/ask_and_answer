# coding=utf-8
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',                        views.index,            name='main_page'),  # список новых вопросов
    path('tag/<str:tag_name>/',     views.tag,              name='tag_page'),
    path('question/',               views.question,         name='question_page'),
    path('ask/',                    views.add_question,     name='ask_page'),
    path('login/', views.signin, name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),

    path('signup/',                 views.signup,           name='signup_page'),
    path('hot/',                    views.hot,              name='hot_page'),
    path('profile/',                views.profile,          name='profile_page'),


    path('like/',                   views.like,             name='like'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
