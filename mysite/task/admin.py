from django.contrib import admin
from .models import ToDoList, Task, Goal

admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(Goal)