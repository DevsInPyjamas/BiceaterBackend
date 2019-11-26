from django.contrib.auth.decorators import login_required

# Create your views here.
import json
from .models import *
from .decorators import returns_json
from django.http import HttpResponseBadRequest, HttpResponse
from .utils import datos_abiertos, check_authorized, throw_bad_request
import re

# READ OPERATIONS

@login_required
@returns_json
def all_users(request):
    check_authorized(request.user)
    query_response = AppUser.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


@login_required
@returns_json
def users_by_username(request, user_input):
    check_authorized(request.user)
    user_input = None
    if request.method == 'GET' and 'user_input' in request.GET:
        user_input = request.GET.get("user_input", '')
    if user_input:
        query_response = AppUser.objects.filter(username__contains=user_input)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


@login_required
@returns_json
def users_by_id(request, user_id):
    check_authorized(request.user)
    if user_id:
        user = User.objects.get(user_id=user_id)
        query_response = AppUser.objects.get(user=user)
        dicted_response = [query_response.to_dict()]
        return dicted_response
    else:
        throw_bad_request()


@login_required
@returns_json
def all_comments(request):
    check_authorized(request.user)
    query_response = Comment.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


@login_required
@returns_json
def comments_by_user_id(request, user_id):
    check_authorized(request.user)
    if user_id:
        query_response = Comment.objects.filter(author=User.objects.get(user_id=user_id))
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


@login_required
@returns_json
def comment_by_stop(request, stop_input):
    check_authorized(request.user)
    stop_input = None
    if request.method == 'GET' and 'stop_input' in request.GET:
        stop_input = request.GET.get("stop_input", '')
    if stop_input:
        query_response = Comment.objects.filter(bike_hire_docking_station_id=stop_input)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


@login_required
@returns_json
def comment_of_comment(request, comment_id):
    check_authorized(request.user)
    if comment_id:
        query_response = Comment.objects.filter(comment_id=comment_id)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()

# CREATE OPERATIONS
@login_required
def create_comment(request):
    check_authorized(request.user)
    text = None
    bike_hire_docking_station_id = None
    if(request.method == 'POST' and 'text' in request.POST
            and 'bike_hire_docking_station_id' in request.POST):
        text = request.POST['text']
        bike_hire_docking_station_id = request.POST['bike_hire_docking_station_id']
    if text and bike_hire_docking_station_id:
        comment = Comment(text=text, author=AppUser.objects.get(user=request.user),
                          bike_hire_docking_station_id=bike_hire_docking_station_id)
        comment.save()
    else:
        throw_bad_request()


# FETCH API DATOS ABIERTOS

@login_required
@returns_json
def fetch_stations(request):
    check_authorized(request.user)
    stations_json = datos_abiertos()
    stations = []
    for element in stations_json:
        location = element['location']['value']
        address = element['address']['value']
        address['streetAddress'] = re.sub(r'[_]+', ' ', element['address']['value']['streetAddress'])
        station_id = element['id'].split(':')[3]
        stations.append({station_id: [location, address]})
    return stations


@login_required
@returns_json
def fetch_station(request, station_id):
    check_authorized(request.user)
    stations_json = datos_abiertos()
    output_dict = [element for element in stations_json if element['id'].split(':')[3] == station_id]
    output_dict = output_dict[0]
    output_dict['address']['value']['streetAddress'] = \
        re.sub(r'[_]+', ' ', output_dict['address']['value']['streetAddress'])
    output_dict['id'] = output_dict['id'].split(':')[3]
    return output_dict
