from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect

__all__ = [
    'signout',
]


def signout(request):
    auth_logout(request)
    messages.success(request, 'Logout Success')
    return redirect('task:index')
