#  hello/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from portfolio.forms import *


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:work'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Login Failed: Your user ID or password is incorrect.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'You were disconnected.'
    })


def bloglist_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def quizz_view(request):
    return render(request, 'portfolio/quizz.html')


def subjectadd_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:subject'))
    context = {'cadeiras': Cadeira.objects.all, 'form': form}
    return render(request, 'portfolio/subjectadd.html', context)


def subject_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/subject.html', context)


def editar_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('bloglist')

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/editar.html', context)


def blogadd_view(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('bloglist')

    context = {'form': form}

    return render(request, 'portfolio/blogadd.html', context)


def layout_view(request):
    return render(request, 'portfolio/layout.html')


def home_view(request):
    return render(request, 'portfolio/home.html')


def login_view(request):
    return render(request, 'portfolio/login.html')


def mainpage_view(request):
    return render(request, 'portfolio/mainpage.html')


def work_view(request):
    return render(request, 'portfolio/work.html')


def chess_view(request):
    return render(request, 'portfolio/chess.html')


def about_view(request):
    return render(request, 'portfolio/about.html')


def contacts_view(request):
    return render(request, 'portfolio/contacts.html')
