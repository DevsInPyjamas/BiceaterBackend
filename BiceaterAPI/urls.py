from django.conf.urls import url
from django.urls import path

from BiceaterAPI import views

urlpatterns = [
    url(r'^users/$', views.all_users, name='All users'),
    url(r'^users/(?P<user_id>[0-9]+)$', views.users_by_id, name='Users by ID'),
    url(r'^users(?P<user_input>\w{0,50})/$', views.users_by_username, name='Users by username'),
    url(r'^users/(?P<user_id>[0-9]+)/comments/taking=(?P<taking>[0-9]+)&page=(?P<page>[0-9]+)$', views.comments_by_user_id, name='Comments by user id'),
    url(r'^users/(?P<user_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)$', views.one_comment_by_user_id, name='Comment by user and comment ids'),
    url(r'^comments/$', views.all_comments, name='All comments'),
    url(r'^comments(?P<stop_input>)/$', views.comment_by_stop, name='Stops comments'),
    url(r'^comments/(?P<comment_id>[0-9]+)/$', views.comment_of_comment, name='Comments of comments'),
    url(r'^stations/(?P<station_id>[0-9]+)/$', views.fetch_station, name='Fetch Station'),
    url(r'^stations/$', views.fetch_stations, name='Fetch All Stations')
]
