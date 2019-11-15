from django.shortcuts import render

# Create your views here.
import json
from .models import *
from django.http import HttpResponseBadRequest, HttpResponse


def all_users(request):
    query_response = User.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return HttpResponse(dicted_response, content_type='json')


def users_by_username(request):
    user_input = None
    if request.method == 'GET' and 'input' in request.GET:
        user_input = request.GET.get("input", '')
    if user_input:
        query_response = User.objects.get(username=user_input)
        dicted_response = [i.to_dict() for i in query_response]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))


def all_comments(request):
    query_response = Comment.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return HttpResponse(dicted_response, content_type='json')


def comments_by_username(request):
    user_input = None
    if request.method == 'GET' and 'input' in request.GET:
        user_input = request.GET.get("input", '')
    if user_input:
        query_response = Comment.objects.filter(author=User.objects.get(username=user_input))
        dicted_response = [i.to_dict() for i in query_response]
        return HttpResponse(dicted_response, content_type='json')
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))
