from django.contrib.auth import authenticate,\
    login as auth_login
from django.shortcuts import redirect, render
from django.contrib import messages

from ..forms import SignInModelForm

__all__ = [
    'signin',
]


def signin(request):
    if request.method == 'POST':
        form = SignInModelForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        user = authenticate(
            email=email,
            password=password,
        )
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Sign In Success')
            return redirect('task:index')
        else:
            messages.error(request, 'Sign In Failed')
            form = SignInModelForm()
            return render(request, 'member/login.html', {'form': form})
    else:
        form = SignInModelForm()
        return render(request, 'member/login.html', {'form': form})
