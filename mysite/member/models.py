from django.db import models
from django.conf import settings


class UserInfo(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='info')
    username = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    exp = models.FloatField(default=float(0))
    dream = models.TextField(blank=True)
    profile_img = models.ImageField(
        null=True,
        upload_to='profile/',
    )

    def __str__(self):
        return self.user.email
