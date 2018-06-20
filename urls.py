from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^sr_users/$', views.index, name='index'),
    url(r'^sr_users/(?P<id>\d+)/$', views.user, name='user'),
    url(r'^sr_users/new/$', views.new, name='new'),
    url(r'^sr_users/(?P<id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^sr_users_/(?P<id>\d+)/destroy/$', views.destroy, name='delete'),
]