from django.conf.urls import include, url

from . import views

app_name = 'web'
urlpatterns = [
    url(r'^ip/(?P<ip_str>.*)/?$', views.details, name='details'),
    url(r'^$', views.index, name='index'),
]
