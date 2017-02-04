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
    'task_check',
]


@login_required()
def to_do_list_new(request, id):
    request.user.todolist_set.create()
    return redirect('task:task_detail', id=request.user.username)


@login_required()
def task_calendar(request):
    _year = {}
    DAY = {
        6: 'Sun',
        0: 'Mon',
        1: 'Tue',
        2: 'Wed',
        3: 'Thu',
        4: 'Fri',
        5: 'Sat',
    }
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
    today = date.today().strftime('%Y%m%d')
    year = int(today[:4])
    _calendar = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(year, 1)
    thisday = int(today[6:])
    thismonth = int(today[4:6])
    LAST_TO_DO_LISTS = {}
    for last_date in range(1, thisday):
        last_to_do_list = ToDoList.objects.filter(date=date(year, thismonth, last_date))
        if last_to_do_list:
            LAST_TO_DO_LISTS[last_date] = last_to_do_list[0]
        else:
            LAST_TO_DO_LISTS[last_date] = None

    result = []
    for num, month_wrap in enumerate(_calendar):
        _year.update({one_year[num + 1]: []})
        for month in month_wrap:
            for week in month:
                _year[one_year[num+1]].append(week)

    for week in _year[one_year[thismonth]]:
        for day in week:
            result.append((day[0], day[1], LAST_TO_DO_LISTS.get(day[0], 0)))

    thisresult = []
    thisresult.append(result[:7])
    thisresult.append(result[7:14])
    thisresult.append(result[14:21])
    thisresult.append(result[21:28])
    thisresult.append(result[28:])

    jan = _year['February']
    context = {
        'month': jan,
        'today': thisday,
        'DAY': ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
        'YEAR': year,
        'thismonth': thismonth,
        'thisresult': thisresult,
    }
    return render(request, 'task/calendar.html', context)


@login_required
def task_detail(request, id):
    context = {}
    try:
        to_do_list = request.user.todolist_set.get(date=date.today())
    except ToDoList.DoesNotExist:
        return render(request, 'task/task_detail.html', context)
    tasks = to_do_list.task_set.all()
    try:
        task_percent = round(to_do_list.task_set.filter(check=True).count()/tasks.count()*100)
    except ZeroDivisionError:
        task_percent = 0
    print(task_percent)
    context['to_do_list'] = to_do_list
    context['tasks'] = tasks
    context['all_task'] = tasks.count()
    context['finish_tasks'] = to_do_list.task_set.filter(check=True).count()
    context['task_percent'] = task_percent
    return render(request, 'task/task_detail.html', context)


@login_required()
def task_new(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.mission = request.user.todolist_set.get(date=date.today())
            task.save()
            return redirect('task:task_detail', id=request.user.username)
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
            return redirect('task:task_detail', id=request.user.username)
    else:
        form = TaskModelForm(instance=task)

    return render(request, 'task/task_edit.html', {'form': form})


@login_required()
def task_check(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.check = not task.check
        task.save()
        return redirect('task:task_detail', id=request.user.username)
    else:
        return redirect('task:index')