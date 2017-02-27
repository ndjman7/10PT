from django.shortcuts import render, redirect

from .models import FutureDiary, RealDiary


def future_diary_create(request):
    if request.method == 'POST':
        FutureDiary.objects.create(user=request.user)
        return redirect('task:task_calendar')


def future_diary_edit(request):
    pass


def real_diary_create(request):
    if request.method == 'POST':
        RealDiary.objects.get_or_create(user=request.user)
        return redirect('task:task_calendar')


def real_diary_edit(request):
    pass
