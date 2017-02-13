from datetime import date
from django.shortcuts import render, redirect

__all__ = [
    'index',
]


def index(request):
    try:
        username = request.user.info.username
    except:
        return render(request, 'common/main.html', {})
    else:
        return redirect('member:personal_page', username=username)

