from django.shortcuts import render, redirect

from member.forms import SignInModelForm

__all__ = [
    'index',
]


def index(request):

    user = request.user

    if user.id is not None:
        return redirect('member:personal_page')
    else:
        return render(request, 'member/signin.html', {'form': SignInModelForm()})


