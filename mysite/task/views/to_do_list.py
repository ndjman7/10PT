import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


from task.models import ToDoList

__all__ = [
    'to_do_list_new',
    'to_do_list_detail',
]


@login_required()
def to_do_list_new(request):
    request.user.todolist_set.create()
    return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))


@login_required
def to_do_list_detail(request, date):
    context = {}
    try:
        # to_do_list = request.user.todolist_set.get(date=date.today())

        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        find_date = datetime.date(year, month, day)
        to_do_list = request.user.todolist_set.get(date=find_date, user=request.user)
    except ToDoList.DoesNotExist:
        return render(request, 'task/to_do_list_detail.html', context)
    tasks = to_do_list.task_set.all()
    try:
        task_percent = round(to_do_list.task_set.filter(check=True).count()/tasks.count()*100)
    except ZeroDivisionError:
        task_percent = 0
    context['to_do_list'] = to_do_list
    context['tasks'] = tasks
    context['all_task'] = tasks.count()
    context['finish_tasks'] = to_do_list.task_set.filter(check=True).count()
    context['task_percent'] = task_percent
    return render(request, 'task/to_do_list_detail.html', context)
