from django.conf.urls import url
from member import views


urlpatterns = [
    url('^login/$', views.signin, name='login'),
    url('^signup/$', views.signup, name='signup'),
    url('^logout/$', views.signout, name='logout'),
]
