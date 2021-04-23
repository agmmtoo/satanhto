from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics')
    description = models.TextField()

    def __str__(self):
        return f'Profile of {self.user.username}'