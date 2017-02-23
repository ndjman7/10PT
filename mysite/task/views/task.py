import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.detail import DetailView

from task.forms import TaskModelForm, TaskEditModelForm
from task.models import Task, ToDoList
from task.utils import TaskCalendar


__all__ = [
    'TaskCheck',
    'task_edit',
    'TaskNew',
    'to_do_list_calendar',
    'TaskDetailView',
    'TaskDelete',
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


@method_decorator(login_required, name='dispatch')
class TaskNew(View):

    def get(self, request, *args, **kwargs):
        today_to_do_list = ToDoList.today_list(user=request.user)
        if not today_to_do_list.can_make_task():
            messages.error(request, 'Task already created')
            return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))

        form = TaskModelForm()
        return render(request, 'task/task_edit.html', {'form': form})

    def post(self, request,  *args, **kwargs):
        today_to_do_list = ToDoList.today_list(user=request.user)
        if not today_to_do_list.can_make_task():
            messages.error(request, 'Task already created')
            return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))

        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.mission = today_to_do_list
            task.ranking = task.mission.ranking
            task.save()
            return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))


@login_required()
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskEditModelForm(data=request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))
    else:
        form = TaskEditModelForm(instance=task)

    return render(request, 'task/task_edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class TaskCheck(View):

    def get(self, request, *args, **kwargs):
        return redirect('task:index')

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=request.POST['task_pk'])
        task.check = not task.check
        task.save()
        return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))


@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView):

    model = Task
    template_name = 'task/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['date'] = self.object.mission.date.strftime('%Y%m%d')
        context['today'] = datetime.date.today().strftime('%Y%m%d')
        return context


@method_decorator(login_required, name='dispatch')
class TaskDelete(View):

    def post(self, request, *args, **kwargs):
        user = request.user
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.mission.user == user:
            change_tasks = task.mission.task_set.filter(ranking__gt=task.ranking)
            for change_task in change_tasks:
                change_task.ranking -= 1
                change_task.save()
            task.delete()
            messages.success(request, '{} delete'.format(task))
        else:
            messages.error(request, 'No access rights')

        return redirect('task:to_do_list_detail', date=datetime.date.today().strftime('%Y%m%d'))


