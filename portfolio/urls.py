#  hello/urls.py

from django.urls import path
from django.shortcuts import render
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.mainpage_view, name='mainpage'),
    path('layout', views.layout_view),
    path('home', views.home_view, name='home'),
    path('mainpage', views.mainpage_view, name='mainpage'),
    path('work', views.work_view, name='work'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('chess', views.chess_view, name='chess'),
    path('subject', views.subject_view, name='subject'),
    path('subjectadd', views.subjectadd_view, name='subjectadd'),
    path('about', views.about_view, name='about'),
    path('contacts', views.contacts_view, name='contacts'),
    path('blogadd', views.blogadd_view, name='blogadd'),
    path('bloglist', views.bloglist_view, name='bloglist'),
    path('quizz', views.quizz_view, name='quizz'),
    path('editar/bloglist', views.bloglist_view, name='bloglist'),
    path('editar/work', views.work_view, name='work'),
    path('editar/about', views.about_view, name='about'),
    path('editar/contacts', views.contacts_view, name='contacts'),
    path('editar/quizz', views.quizz_view, name='quizz'),
    path('editar/subject', views.subject_view, name='subject'),
    path('editar/subjectadd', views.subject_view, name='subject'),
    path('editar/<int:post_id>', views.editar_view, name='editar'),
]
