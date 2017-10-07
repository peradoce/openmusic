from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import *
from django.contrib.auth.models import User
from main.models import *
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.core.mail import send_mail
import hashlib
from django.contrib.auth.hashers import make_password
import datetime
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.

def addMusic(request):
    if request.method == 'POST':
        title = 'OpenMusic - Add Music'
        form = AddMusicForm(request.POST)
        success_msg = False
        get_genre_all = Genre.objects.order_by("genre")
        if form.is_valid():
            cd = form.cleaned_data
            genre = request.POST['genre']
            get_genre = Genre.objects.get(id=genre)
            AddMusic.objects.create(title=cd['title'], code=cd['code'],
            genre=get_genre)
            success_msg = True
        return render(request, 'front/addmusic.html',
        {'title':title, 'success_msg':success_msg, 'form':form,
        'genre':get_genre_all})
    else:
        title = 'OpenMusic - Add Music'
        form = AddMusicForm()
        success_msg = False
        get_genre = Genre.objects.order_by("genre")
        return render(request, 'front/addmusic.html',
        {'title':title, 'success_msg':success_msg, 'form':form,
        'genre':get_genre})
