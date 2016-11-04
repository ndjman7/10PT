import calendar
import datetime
from django.shortcuts import render, redirect, get_object_or_404

from task.forms import TaskModelForm
from task.models import Task

__all__ = [
    'task_calendar',
    'task_detail',
    'task_edit',
    'task_new',
]


def task_calendar(request):
    c = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(2016, 1)
    return render(request, 'task/calendar.html', {'year': c})


def task_detail(request):
    try:
        task = request.user.task_set.get(date=datetime.date.today())
    except Task.DoesNotExist:
        return redirect('task:task_new')
    tasks = task.tasks

    return render(request, 'task/task_detail.html', {'tasks': tasks})


def task_new(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task:task_detail')
    else:
        form = TaskModelForm()
        return render(request, 'task/task_edit.html', {'form': form})


def task_edit(request):
    task = get_object_or_404(Task, date=datetime.date.today())
    if request.method == 'POST':
        form = TaskModelForm(data=request.POST, instance=task)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task:task_detail')
    else:
        form = TaskModelForm(instance=task)

    return render(request, 'task/task_edit.html', {'form': form})