from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


__all__ = [
    'to_do_list_new',
]


@login_required()
def to_do_list_new(request, id):
    request.user.todolist_set.create()
    return redirect('task:task_detail', id=request.user.username)


