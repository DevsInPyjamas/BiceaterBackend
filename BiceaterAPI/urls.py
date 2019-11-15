from django.conf.urls import url
from django.urls import path

from BiceaterAPI import views

urlpatterns = [
    url(r'^users(?P<user_input>\w{0,50})$', views.users_by_username, name='Users by username'),
    url(r'^users(?P<user_id>[0-9]+)$', views.users_by_id, name='Users by ID'),
    url(r'^users/$', views.all_users, name='All users')
]
