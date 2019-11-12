from django.conf.urls import url
from BiceaterAPI import views

urlpatterns = [
    url(r'^users$', views.all_users, name='All users'),
    url(r'^users/(?P<input>\w{0,50})/$', views.users_by_username, name='Users by username')
]
