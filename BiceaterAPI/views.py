from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
import json
from .models import *
from .decorators import returns_json
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse
from .utils import datos_abiertos


@login_required
@returns_json
def all_users(request):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    query_response = AppUser.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


@login_required
@returns_json
def users_by_username(request, user_input):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    user_input = None
    if request.method == 'GET' and 'user_input' in request.GET:
        user_input = request.GET.get("user_input", '')
    if user_input:
        query_response = AppUser.objects.filter(username__contains=user_input)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


@login_required
@returns_json
def users_by_id(request, user_id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    if user_id:
        query_response = AppUser.objects.get(user_id=user_id)
        dicted_response = [query_response.to_dict()]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


@login_required
@returns_json
def all_comments(request):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    query_response = Comment.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


@login_required
@returns_json
def comments_by_user_id(request, user_id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    if user_id:
        query_response = Comment.objects.filter(author=User.objects.get(user_id=user_id))
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


@login_required
@returns_json
def comment_by_stop(request, stop_input):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    stop_input = None
    if request.method == 'GET' and 'stop_input' in request.GET:
        stop_input = request.GET.get("stop_input", '')
    if stop_input:
        query_response = Comment.objects.filter(bike_hire_docking_station_id=stop_input)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


@login_required
@returns_json
def comment_of_comment(request, comment_id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    if comment_id:
        query_response = Comment.objects.filter(comment_id=comment_id)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


@login_required
@returns_json
def fetch_stations(request):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    stations_json = datos_abiertos()
    stations = []
    for element in stations_json:
        location = element['location']['value']
        address = element['address']['value']
        station_id = element['id'].split(':')[3]
        stations.append({station_id: [location, address]})
    return stations


@login_required
@returns_json
def fetch_station(request, station_id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    stations_json = datos_abiertos()
    output_dict = [element for element in stations_json if element['id'].split(':')[3] == station_id]
    return output_dict[0]
