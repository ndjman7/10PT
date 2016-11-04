from django.conf.urls import url
from member import views


urlpatterns = [
    url('^login/$', views.login, name='login'),
    url('^signup/$', views.signup, name='signup'),
    url('^logout/$', views.logout, name='logout'),
]
