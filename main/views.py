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
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator
# Create your views here.

def PlaylistView(request):
    title = 'OpenMusic - Generate Playlist'
    form = GeneratePlaylistForm()
    get_genre = Genre.objects.order_by("genre")
    return render(request, 'front/generateplaylist.html', {'title':title, 'form':form,
    'genre':get_genre})

def PlaylistFormAjax(request):
    output = {}
    done = False
    playlist_name = request.POST.get('title', False)
    description = request.POST.get('description', False)
    email = request.POST.get('email', False)
    genre = request.POST.get('genre', None)
    ###creating key using hash###
    date = timezone.now
    ran_gen = randint(10000, 10000000)
    string_generated = 'Kaka %s %s' % (date, ran_gen)
    date_to_string = str(ran_gen).encode('utf-8')
    hash_object = hashlib.sha256(date_to_string)
    hex_dig = hash_object.hexdigest()
    final_key = hex_dig[:12]
    ###end creating key###
    if playlist_name == '':
        msg_1 = 'Empty Music Name, insert a music name.<br>'
        output = {'msg_1':msg_1}
    if description == '':
        msg_2 = {'msg_2':'Empty description, insert a description.<br>'}
        output.update(msg_2)
    if email == '':
        msg_4 = {'msg_4':'Empty e-mail, insert a e-mail.<br>'}
        output.update(msg_2)
    if genre == '':
        msg_3 = {'msg_3':'Empty Genre, insert a genre.<br>'}
        output.update(msg_3)
    elif genre == 0:
        msg_3 = {'msg_3':'Empty Genre, insert a genre.<br>'}
        output.update(msg_3)
    if len(output) > 0:
        done = True
    else:
        get_genre = Genre.objects.get(id=genre)
        Playlist.objects.create(title=playlist_name, description=description,
        genre=get_genre, key=final_key)
        send_mail(
        'Playlist Data - OpenMusic',
        'Playlist Name: %s \n Playlist Description: %s \n Playlist Key: %s' % (playlist_name, description, final_key),
        'noreply.openmusic@gmail.com',
        [email],
        fail_silently=False,
        )
        output = {'final_key':final_key}
        success_msg = {'success_msg':'Playlist Generated successfully.'}
        output.update(success_msg)
    return JsonResponse(output)

def listMusic(request):
    title = 'OpenMusic - Music List'
    first_music = Music.objects.order_by("id")[:1]
    music_list = Music.objects.order_by("-id")
    page = request.GET.get('page', 1)
    paginator = Paginator(music_list, 12)

    try:
        musics = paginator.page(page)
    except PageNotAnInteger:
        musics = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'front/listmusic.html', {'title':title, 'musics':musics, 'first_music':first_music})
