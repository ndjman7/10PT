from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User)
    task1 = models.CharField(max_length=50, blank=True, null=True)
    task2 = models.CharField(max_length=50, blank=True, null=True)
    task3 = models.CharField(max_length=50, blank=True, null=True)
    task4 = models.CharField(max_length=50, blank=True, null=True)
    task5 = models.CharField(max_length=50, blank=True, null=True)
    task6 = models.CharField(max_length=50, blank=True, null=True)
    task7 = models.CharField(max_length=50, blank=True, null=True)
    task8 = models.CharField(max_length=50, blank=True, null=True)
    task9 = models.CharField(max_length=50, blank=True, null=True)
    task10 = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "date"),)

    def __str__(self):
        return str(self.date)

    @property
    def tasks(self):
        tasks = []
        tasks.append(self.task1)
        tasks.append(self.task2)
        tasks.append(self.task3)
        tasks.append(self.task4)
        tasks.append(self.task5)
        tasks.append(self.task6)
        tasks.append(self.task7)
        tasks.append(self.task8)
        tasks.append(self.task9)
        tasks.append(self.task10)
        return tasks
