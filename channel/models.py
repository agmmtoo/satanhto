from django.db import models

from sauce.ImageUploadLocation import user_dir

class Channel(models.Model):
    name = models.CharField(max_length=250, help_text='Just in case, be unique!')
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to=user_dir, blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text='Optional url field')
    description = models.TextField(help_text='You might want to let ppl know some infos \'bout your channel. Markdown is supported here.')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name