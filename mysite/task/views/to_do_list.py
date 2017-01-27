import calendar
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from task.forms import TaskModelForm
from task.models import Task, ToDoList

__all__ = [
    'to_do_list_new',
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
    _year = {}
    one_year = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }
    year = 2017
    _calendar = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(year, 1)
    today = date.today().strftime('%m%d')
    day = int(today[2:])

    for num, month_wrap in enumerate(_calendar):
        _year.update({one_year[num + 1]: []})
        for month in month_wrap:
            for week in month:
                _year[one_year[num + 1]].append(week)
    jan = _year['January']
    context = {
        'month': jan,
        'today': day,
    }
    return render(request, 'task/calendar.html', context)


@login_required
def task_detail(request):
    context = {}
    try:
        to_do_list = request.user.todolist_set.get(date=date.today())
    except ToDoList.DoesNotExist:
        return render(request, 'task/task_detail.html', context)
    tasks = to_do_list.task_set.all()
    context['to_do_list'] = to_do_list
    context['tasks'] = tasks
    return render(request, 'task/task_detail.html', context)


@login_required()
def task_new(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.mission = request.user.todolist_set.get(date=date.today())
            task.save()
            return redirect('task:task_detail')
    else:
        form = TaskModelForm()
        return render(request, 'task/task_edit.html', {'form': form})


@login_required()
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
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
