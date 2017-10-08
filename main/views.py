from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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
    title = 'OpenMusic - Add Music'
    form = AddMusicForm()
    get_genre = Genre.objects.order_by("genre")
    return render(request, 'front/addmusic.html',
    {'title':title, 'form':form,
    'genre':get_genre})

def addMusicAjax(request):
    output = {}
    error = {}
    i = 0
    music_name = request.POST.get('title', False);
    code = request.POST.get('code', False);
    genre = request.POST.get('genre', None)
    if music_name == '':
        error[0] = 'Empty Music Name, insert a music name.<br>'
    if code == '':
        error[1] = 'Empty Code, insert a youtube video code.<br>'
    if genre == '':
        error[2] = 'Empty Genre, insert a genre.<br>'
    elif genre == 0:
        error[3] = 'Empty Genre, insert a genre.<br>'
    if len(error) > 0:
        for errors in error:
            output[i] = errors
            i = i+1;
    else:
        get_genre = Genre.objects.get(id=genre)
        AddMusic.objects.create(title=music_name, code=code,
        genre=get_genre)
        success_msg = 'Music added successfully.'
        output = {'success_msg':success_msg}
    return JsonResponse(output)

def PlaylistView(request):
    title = 'OpenMusic - Generate Playlist'
    form = GeneratePlaylistForm()
    get_genre = Genre.objects.order_by("genre")
    return render(request, 'front/generateplaylist.html', {'title':title, 'form':form,
    'genre':get_genre})
