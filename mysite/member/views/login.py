from django.contrib.auth import authenticate,\
    login as auth_login
from django.shortcuts import redirect, render
from django.contrib import messages

__all__ = [
    'login',
]


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return redirect('member:login')
        user = authenticate(
            email=email,
            password=password
        )
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login Success')
            return redirect('task:index')
        else:
            messages.error(request, 'Login failed')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})
