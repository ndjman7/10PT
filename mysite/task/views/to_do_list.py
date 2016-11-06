import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from task.forms import TaskModelForm
from task.models import Task, ToDoList

__all__ = [
    'task_calendar',
    'task_detail',
    'task_edit',
    'task_new',
]


@login_required()
def to_do_list_new(request):
    request.user.todolist_set.create()
    return redirect('task:task_detail')


@login_required()
def task_calendar(request):
    c = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(2016, 1)
    return render(request, 'task/calendar.html', {'year': c})


@login_required
def task_detail(request):
    context = {}
    try:
        to_do_list = request.user.todolist_set.get(date=datetime.date.today())
    except ToDoList.DoesNotExist:
        return redirect('task:to_do_list')
    tasks = ToDoList.task_set.all()
    context['to_do_list'] = to_do_list
    context['tasks'] = tasks
    return render(request, 'task/task_detail.html', context)


@login_required()
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


@login_required()
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