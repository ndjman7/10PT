from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from ..models import UserInfo


__all__= [
    'personal_page',
]


def personal_page(request):

    context = {}
    try:
        user_info = UserInfo.objects.get(username=request.user.info.username)

    except UserInfo.DoesNotExist:
        return redirect('task:index')

    return render(request, 'member/user_detail.html', context)


