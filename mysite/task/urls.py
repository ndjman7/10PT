from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^to_do_list/new/$', views.to_do_list_new, name='to_do_list_new'),
    url(r'^to_do_list/(?P<id>[a-z0-9]+)/$', views.to_do_list_detail, name='to_do_list_detail'),
    url(r'^task/$', views.task_calendar, name='task_calendar'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^task/edit/(?P<pk>[0-9]+)/$', views.task_edit, name='task_edit'),
    url(r'^task/check/(?P<pk>[0-9]+)/$', views.task_check, name='task_check'),
]
