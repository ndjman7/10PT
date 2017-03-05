from django.shortcuts import render
from django.views.generic import ListView

from ..models import Goal

__all__ = [
    'GoalList',
    'goal_main',
]


class GoalList(ListView):

    model = Goal
    template_name = 'task/goal_list.html'


def goal_main(request):
    context = {}
    return render(request, 'task/goal_main.html', context)