# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # список новых вопросов
    path('<int:page_num>', views.index, name='question_list'),  # список новых вопросов
    path('tag/', views.tag),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('tag/<str:tag_name>/<int:page_num>', views.tag, name='tag_list'),
    path('question/', views.question),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask/', views.ask),
    path('login/', views.login),
    path('signup/', views.signup),
    path('hot/', views.hot),
    path('hot/<int:page_num>/', views.hot, name='hot_list'),
    path('profile/<int:user_id>/', views.profile, name='profile')
]
