import datetime

from django.conf import settings
from django.db import models


class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "date"),)

    def __str__(self):
        return str(self.date)

    def can_make_task(self):
        if self.task_set.count() < 10:
            return True
        else:
            return False

    @property
    def ranking(self):
        return self.task_set.count() + 1

    @classmethod
    def today_list(cls, user):
        return cls.objects.get(user=user, date=datetime.date.today())


class Task(models.Model):
    mission = models.ForeignKey(ToDoList)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    check = models.BooleanField(default=False)
    ranking = models.IntegerField(null=True)

    def __str__(self):
        return str(self.title)
