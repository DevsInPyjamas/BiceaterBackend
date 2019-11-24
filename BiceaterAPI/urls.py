from django.conf.urls import url
from django.urls import path

from BiceaterAPI import views

urlpatterns = [
    url(r'^comments(?P<stop_input>)/$', views.comment_by_stop, name='Stops comments'),
    url(r'^comments/(?P<comment_id>[0-9]+)/$', views.comment_of_comment, name='Comments of comments'),
    url(r'^users/(?P<user_id>[0-9]+)$', views.users_by_id, name='Users by ID'),
    url(r'^users/$', views.all_users, name='All users'),
    url(r'^users/(?P<user_input>\w{0,50})/$', views.users_by_username, name='Users by username'),
    url(r'^comments$', views.all_comments, name='All comments'),
    url(r'^comments/(?P<user_id>[0-9]+)$', views.comments_by_user_id, name='Comments by user id'),
    path('', views.malaga_Api, name='malaga_Api'),
]
