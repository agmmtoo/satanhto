from django.db import models
from django.conf import settings

from django.conf import settings

from .ImageUploadLocation import user_dir

class Series(models.Model):
    name = models.CharField(max_length=250)
    hepburn = models.CharField(max_length=250, help_text='Japanese name written in English')
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    cover = models.ImageField(upload_to=user_dir, blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='series_created', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.name)
    
    class Meta:
        ordering = ('-created',)

class Season(models.Model):
    series = models.ForeignKey(Series, related_name='seasons', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='Season ', help_text='Season 1, Season 2, etc. (use space for consistency)')
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Episode(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='episodes_uploaded', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='If no title available, user Episode 1, 2 etc.')
    slug = models.SlugField(max_length=250)
    order = models.PositiveIntegerField(help_text='This value is used for ordering episodes')

    file = models.FileField(upload_to=user_dir)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title
        