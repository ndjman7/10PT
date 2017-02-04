from django.conf.urls import url
from motivation import views


urlpatterns = [
    url('^post/$', views.PostView.as_view(), name='post')
]