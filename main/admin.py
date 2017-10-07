from django.contrib import admin
from .models import *

# Register your models here.

class AddMusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', )

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre', )


admin.site.register(AddMusic, AddMusicAdmin)
admin.site.register(Genre, GenreAdmin)
