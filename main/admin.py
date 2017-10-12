from django.contrib import admin
from .models import *

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre', )

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', )

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', )

class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Music, MusicAdmin)
