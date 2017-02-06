from datetime import date
from django.shortcuts import render


__all__ = [
    'index',
]


def index(request):
    today = date.today().strftime('%Y%m%d')
    return render(request, 'common/index.html', {'today': today})