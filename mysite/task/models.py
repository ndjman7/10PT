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
    PROGRESS_CHOICES = (
        ('A', '#1e6823'),
        ('B', '#44a340'),
        ('C', '#8cc665'),
        ('D', '#d6e685'),
        ('F', '#eeeeee'),
    )
    mission = models.ForeignKey(ToDoList)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    check = models.BooleanField(default=False)
    ranking = models.IntegerField(null=True)
    progress = models.CharField(max_length=7, choices=PROGRESS_CHOICES, default='A')

    def __str__(self):
        return str(self.title)

    def sort_ranking(self, origin_ranking):

        to_do_list = self.mission
        if self.ranking == origin_ranking:
            return

        if self.ranking < origin_ranking:
            change_tasks = to_do_list.task_set.filter(ranking__gte=self.ranking).filter(ranking__lt=origin_ranking)
            for change_task in change_tasks:
                change_task.ranking += 1
                change_task.save()
        else:
            change_tasks = to_do_list.task_set.filter(ranking__lte=self.ranking).filter(ranking__gt=origin_ranking)
            for change_task in change_tasks:
                change_task.ranking -= 1
                change_task.save()

    def set_progress(self):
        progress = self.mission.task_set.filter(check=True).count()
        if progress == 0:
            self.progress = 'F'
        elif 1 <= progress <= 2:
            self.progress = 'D'
        elif 3 <= progress <= 5:
            self.progress = 'C'
        elif 6 <= progress <= 8:
            self.progress = 'B'
        elif 9 <= progress <= 10:
            self.progress = 'A'
        self.save()
