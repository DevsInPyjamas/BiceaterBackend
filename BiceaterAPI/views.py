from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponseBadRequest
from BiceaterAPI import models


def all_users(request):
    query_response = models.User.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


def users_by_username(request):
    user_input = None
    if request.method == 'GET' and 'id' in request.GET:
        user_input = request.GET.get("input", '')
    if user_input:
        query_response = models.User.objects.get(username=user_input)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
        return HttpResponseBadRequest(json.dumps(error_str))
