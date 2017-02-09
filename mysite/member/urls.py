from django.conf.urls import url
from member import views


urlpatterns = [
    url('^signin/$', views.signin, name='signin'),
    url('^signup/$', views.signup, name='signup'),
    url('^signout/$', views.signout, name='signout'),
]
