from django.shortcuts import render, redirect
from django.contrib import messages
from member.forms import SignUpModelForm

__all__ = [
    'signup',
]


def signup(request):
    if request.method == 'POST':
        form = SignUpModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ID Created')
            return redirect('member:login')
        messages.error(request, 'ID Not Created')
        form = SignUpModelForm()
    else:
        form = SignUpModelForm()
    return render(request, 'member/signup.html', {'form': form})
