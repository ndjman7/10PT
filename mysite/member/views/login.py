from django.contrib.auth import authenticate,\
    login as auth_login
from django.shortcuts import redirect, render

__all__ = [
    'login',
]


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return redirect('member:login')
        user = authenticate(
            username=username,
            password=password
        )
        print(user)
        if user is not None:
            print("a")
            auth_login(request, user)
            return redirect('task:index')
        else:
            print("일로빠진다?")
            return render(request, 'member/login.html', {})
    else:
        print("c")
        return render(request, 'member/login.html', {})
