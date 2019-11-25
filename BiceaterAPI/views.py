from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
import json
from .models import *
from .decorators import returns_json
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse


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
def comments_list(request, author):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    query_response = Comment.objects.filter(author=author)
    queryfilter = int(request.GET.get('taking'))
    paginator = Paginator(query_response, queryfilter)
    page = request.GET.get('page')
    return HttpResponse(paginator, content_type='json')


@login_required
@returns_json
def datos_Abiertos(request):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    response = request.get(
        'https://datosabiertos.malaga.eu/recursos/transporte/EMT/EMTocupestacbici/ocupestacbicifiware.json')
    malaga = response.json()
    return HttpResponse(request, malaga, {
        'status': malaga['status'],
        'totalSlotNumber': malaga['totalSlotNumber'],
        'availableBikeNumber': malaga['availableBikeNumber'],
        'freeSlotNumber': malaga['freeSlotNumber'],
        'location': malaga['location'],
        'address': malaga['address'],
        'type': malaga['type'],
        'id': malaga['id'],
    })
