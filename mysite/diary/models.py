from django.db import models
from django.conf import settings


class FutureDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        unique_together = (('user', 'date'),)

    def __str__(self):
        return "{} {}'s FutureDiary".format(self.date, self.user)


class RealDiary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        unique_together = (('user', 'date'),)

    def __str__(self):
        return "{} {}'s RealDiary".format(self.date, self.user)
