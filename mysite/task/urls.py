from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^task/$', views.task_calendar, name='task_calendar'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^task/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/detail/$', views.task_detail, name='task_detail'),
]
