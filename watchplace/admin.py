from django.contrib import admin

from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'series', 'body', 'created']
    list_filter = ['user', 'series', 'created']
    search_fields = ['body',]