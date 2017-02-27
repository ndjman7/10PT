from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^to_do_list/new/$', views.to_do_list_new, name='to_do_list_new'),
    url(r'^to_do_list/(?P<date>[0-9]+)/$', views.to_do_list_detail, name='to_do_list_detail'),


    url(r'^task$', views.to_do_list_calendar, name='task_calendar'),
    url(r'^task/(?P<date>[0-9]+)$', views.to_do_list_calendar, name='task_calendar_detail'),
    url(r'^task/new/$', views.TaskNew.as_view(), name='task_new'),
    url(r'^task/edit/(?P<pk>[0-9]+)/$', views.task_edit, name='task_edit'),
    url(r'^task/check$', views.TaskCheck.as_view(), name='task_check'),
    url(r'^task/detail/(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^task/delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='task_delete'),

    url(r'^goal$', views.GoalList.as_view(), name='goal_list'),
]
