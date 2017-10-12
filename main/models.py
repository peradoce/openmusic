from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=75)
    icon = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.genre

class Artist(models.Model):
    name = models.CharField(max_length=75)
    facebook = models.CharField(null=True, blank=True, max_length=250)
    twitter = models.CharField(null=True, blank=True, max_length=250)
    youtube = models.CharField(null=True, blank=True, max_length=250)
    wiki = models.CharField(null=True, blank=True, max_length=250)
    bio = models.TextField(max_length=300)
    image = models.FileField(upload_to='artist_images')

    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=125)
    music_file = models.FileField(upload_to='musics')
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField(max_length=300)
    key = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.title

class PlaylistMusic(models.Model):
    playlist_key = models.CharField(max_length=250)
    music = models.ForeignKey(Music)


class PlaylistVote(models.Model):
    playlist = models.ForeignKey(Playlist)
    vote_up = models.IntegerField()
    vote_down = models.IntegerField()
