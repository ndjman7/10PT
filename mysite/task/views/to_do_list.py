import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from task.models import ToDoList
from task.utils import TaskCalendar

__all__ = [
    'to_do_list_new',
    'to_do_list_detail',
]


@login_required()
def to_do_list_new(request):
    request.user.todolist_set.create()
    return redirect('task:task_calendar', date=TaskCalendar.today_to_str())


@login_required
def to_do_list_detail(request, date):
    context = {}
    try:
        year = TaskCalendar.this_year
        month = TaskCalendar.this_month
        day = TaskCalendar.this_day
        find_date = datetime.date(year, month, day)
        to_do_list = request.user.todolist_set.get(date=find_date, user=request.user)
    except ToDoList.DoesNotExist:
        return render(request, 'task/to_do_list_detail.html', context)
    tasks = to_do_list.task_set.order_by('ranking')
    try:
        task_percent = round(to_do_list.task_set.filter(check=True).count()/tasks.count()*100)
    except ZeroDivisionError:
        task_percent = 0
    all_task = tasks.count()
    finish_tasks = to_do_list.task_set.filter(check=True).count()
    context['to_do_list'] = to_do_list
    context['tasks'] = tasks
    context['all_task'] = all_task
    context['finish_tasks'] = finish_tasks
    context['task_percent'] = task_percent
    context['date'] = date
    context['today'] = TaskCalendar.today_to_str()
    context['success'] = True if all_task - finish_tasks == 0 and all_task > 0 else False
    return render(request, 'task/to_do_list_detail.html', context)
