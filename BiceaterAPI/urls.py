from django.conf.urls import url
from django.urls import path

from BiceaterAPI import views

urlpatterns = [
    url(r'^users/me/?$', views.me, name='My User ID'),
    url(r'^users/?$', views.all_users, name='All users'),
    url(r'^users/(?P<user_id>[0-9]+)/?$', views.users_by_id, name='Users by ID'),
    url(r'^users/(?P<user_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/?$', views.one_comment_by_user_id,
        name='Comment by user and comment ids'),
    url(r'^users/(?P<user_id>[0-9]+)/comments/?$', views.comments_by_user_id, name='Comments by user id'),
    url(r'^comments/?$', views.all_comments, name='All comments'),
    url(r'^comments(?P<stop_input>)/?$', views.comment_by_stop, name='Stops comments'),
    url(r'^comments/(?P<comment_id>[0-9]+)/?$', views.comment_of_comment, name='Comments of comments'),
    url(r'^comments/(?P<comment_id>[0-9]+)/delete/?$', views.delete_comment, name='Comments of comments'),
    url(r'^stations/(?P<station_id>[0-9]+)/?$', views.fetch_station, name='Fetch Station'),
    url(r'^stations/?$', views.fetch_stations, name='Fetch All Stations'),
    url(r'^stations/(?P<station_id>[0-9]+)/comments/?$', views.comments_by_station_id, name='Comments by station'),
    url(r'^comments/create/?$', views.create_comment, name="Create new comment"),
    url(r'^users/update/?$', views.update_user, name="Update user"),
    url(r'^routes/calculate/?$', views.calculate_best_route, name='Routing calculation'),
    url(r'^logout/?$', views.logout, name='logout'),
    url(r'^stations/search/?', views.search_station_by_address, name='Search station by address'),
    url(r'^rating/create/?$', views.create_rating, name='Create new rating'),
    url(r'^rating/average/(?P<station_id>[0-9]+)?$', views.rating_average, name='Rating average'),
    url(r'^comments/(?P<comment_id>[0-9]+)/comment/$', views.comments_parameters, name='Comment parameters'),
    url(r'^comments/(?P<comment_id>[0-9]+)/responses/$', views.comments_responses, name='Comment responses'),
    url(r'^users/(?P<string>)/$', views.users_parameters, name='User parameters'),
]
