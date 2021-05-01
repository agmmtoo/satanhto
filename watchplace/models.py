from django.db import models
from django.conf import settings

from sauce.models import Series

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    series = models.ForeignKey(Series, related_name='comments', on_delete=models.CASCADE)

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user.username}\'s comment on {self.series}'