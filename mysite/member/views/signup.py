from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from member.forms import SignUpModelForm


__all__ = [
    'signup',
]


def signup(request):
    if request.method == 'POST':
        form = SignUpModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member:login')
        form = SignUpModelForm()
    else:
        form = SignUpModelForm()
    return render(request, 'member/signup.html', {'form': form})
