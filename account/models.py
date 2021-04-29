from django.db import models
from django.conf import settings

from channel.models import Channel

from sauce.ImageUploadLocation import user_dir

class Profile(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, help_text='yy-mm-dd, Optional')
    picture = models.ImageField(upload_to=user_dir)
    description = models.TextField(help_text='Bio...or smth like that.')

    channel = models.ForeignKey(Channel, blank=True, null=True, related_name='members', on_delete=models.DO_NOTHING)
    # Do_NOTHIG Profile on Channel deletion

    def __str__(self):
        return f'Profile of {self.owner.username}'