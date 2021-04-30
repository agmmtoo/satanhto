from django.contrib import admin

from .models import Channel
from account.admin import ProfileInline

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'logo', 'link', 'description', 'created', 'updated']
    search_fields = ['name',]
    inlines = [ProfileInline,]