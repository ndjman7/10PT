import calendar
from django.shortcuts import render


def index(request):
    return render(request, 'common/index.html', {})


def task_calendar(request):
    c = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(2016, 1)
    return render(request, 'task/calendar.html', {'year': c})


