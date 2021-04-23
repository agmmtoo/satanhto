from django.contrib import admin

from .models import Series, Season, Episode

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'hepburn', 'slug', 'cover', 'created', 'updated']
    prepopulated_fields = {'slug': ('hepburn',)}

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'order', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}