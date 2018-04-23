# coding=utf-8
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),  # список новых вопросов
    path('<int:page_num>', views.index, name='question_list'),  # список новых вопросов
    path('tag/', views.tag, name='empty_tag'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('tag/<str:tag_name>/<int:page_num>', views.tag, name='tag_list'),
    path('question/', views.question, name='empty_question'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask/', views.add_question, name='ask_page'),
    path('login/', views.login, name='login_page'),
    path('signup/', views.signup, name='signup_page'),
    path('hot/', views.hot, name='hot_page'),
    path('hot/<int:page_num>/', views.hot, name='hot_list'),
    path('profile/<int:user_id>/', views.profile, name='profile'),

    path('like/', views.like, name='like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
