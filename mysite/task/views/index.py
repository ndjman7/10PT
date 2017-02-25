from django.shortcuts import render, redirect

from member.forms import SignUpModelForm

__all__ = [
    'index',
]


def index(request):
    try:
        username = request.user.info.username
    except:
        return render(request, 'common/main.html', {'form': SignUpModelForm()})
    else:
        return redirect('member:personal_page', username=username)

