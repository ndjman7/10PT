import calendar
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView

from task.forms import TaskModelForm
from task.models import Task, ToDoList
from task.utils import TaskCalendar


__all__ = [
    'task_check',
    'task_edit',
    'task_new',
    'to_do_list_calendar',
    'TaskDetailView',
]


@login_required()
def to_do_list_calendar(request):

    today = TaskCalendar.today
    this_year = TaskCalendar.this_year
    this_day = TaskCalendar.this_day
    this_month = TaskCalendar.this_month

    result, _year = TaskCalendar.month_list(ToDoList, request.user)
    this_month_list = TaskCalendar.pack_one_week(result)

    context = {
        'thisday': this_day,
        'DAY': TaskCalendar.DAY.values(),
        'YEAR': this_year,
        'thismonth': this_month,
        'thisresult': this_month_list,
        'today': today,
    }
    return render(request, 'task/calendar.html', context)


@login_required()
def task_new(request):
    today_to_do_list = request.user.todolist_set.get(date=datetime.date.today(), user=request.user)
    if not today_to_do_list.can_make_task():
        messages.error(request, 'Task already created')
        return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.mission = today_to_do_list
            task.save()
            return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))
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
            return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))
    else:
        form = TaskModelForm(instance=task)

    return render(request, 'task/task_edit.html', {'form': form})


@login_required()
def task_check(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.check = not task.check
        task.save()
        return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))
    else:
        return redirect('task:index')


class TaskDetailView(DetailView):

    model = Task
    template_name = 'task/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['date'] = self.object.mission.date.strftime('%Y%m%d')
        context['today'] = datetime.date.today().strftime('%Y%m%d')
        return context
