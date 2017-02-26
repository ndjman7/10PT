from django.views.generic import ListView

from ..models import Goal

__all__ = [
    'GoalList',
]


class GoalList(ListView):

    model = Goal
    template_name = 'task/goal_list.html'
