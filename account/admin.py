from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['owner', 'date_of_birth', 'picture', 'description']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)