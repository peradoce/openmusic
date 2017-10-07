from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=75)
    icon = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.genre

class AddMusic(models.Model):
    title = models.CharField(max_length=125)
    code = models.CharField(max_length=50)
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
    music = models.ForeignKey(AddMusic)


class PlaylistVote(models.Model):
    playlist = models.ForeignKey(Playlist)
    vote_up = models.IntegerField()
    vote_down = models.IntegerField()

class Report(models.Model):
    music = models.ForeignKey(AddMusic)
    date = models.DateField()
    status = models.CharField(max_length=50)
