from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
import json
from .models import *
from django.http import HttpResponseBadRequest, HttpResponse


def all_users(request):
    query_response = User.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return HttpResponse(dicted_response, content_type='json')


def users_by_username(request, user_input):
    user_input = None
    if request.method == 'GET' and 'user_input' in request.GET:
        user_input = request.GET.get("user_input", '')
    if user_input:
        query_response = User.objects.filter(username__contains=user_input)
        dicted_response = [i.to_dict() for i in query_response]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


def users_by_id(request, user_id):
    if user_id:
        query_response = User.objects.get(user_id=user_id)
        dicted_response = [query_response.to_dict()]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


def all_comments(request):
    query_response = Comment.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return HttpResponse(dicted_response, content_type='json')


def comments_by_user_id(request, user_id):
    if user_id:
        query_response = Comment.objects.filter(author=User.objects.get(user_id=user_id))
        dicted_response = [i.to_dict() for i in query_response]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


def comment_by_stop(request, stop_input):
    stop_input = None
    if request.method == 'GET' and 'stop_input' in request.GET:
        stop_input = request.GET.get("stop_input", '')
    if stop_input:
        query_response = Comment.objects.filter(bike_hire_docking_station_id=stop_input)
        dicted_response = [i.to_dict() for i in query_response]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


def comment_of_comment(request, comment_id):
    if comment_id:
        query_response = Comment.objects.filter(comment_id=comment_id)
        dicted_response = [i.to_dict() for i in query_response]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))

@returns_json
@with_session
def comments_list(request, author):
    query_response = Comment.objects.filter(author=author)
    queryfilter = int(request.GET.get('query_response', 10))
    paginator = Paginator(query_response, queryfilter)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    return HttpResponse(paginator, content_type='json')


def datos_Abiertos(request):
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
