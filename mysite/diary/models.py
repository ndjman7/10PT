from django.db import models
from django.conf import settings


class FutureDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        unique_together = (('user', 'date'),)


class RealDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        unique_together = (('user', 'date'),)
