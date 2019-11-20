import json
from django.http import HttpResponse
from BiceaterAPI import models


def returns_json(func):
    def returns_json_decorator(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            response['Content-Type'] = 'application/json; charset=utf-8'
        else:
            response = HttpResponse(json.dumps(response))
            response['Content-Type'] = 'application/json; charset=utf-8'
        return response

    return returns_json_decorator


def with_session(func):
    def with_session_decorator(request):
        if 'HTTP_X_SESSION_USER' in request.META:
            header_request = request.META['HTTP_X_SESSION_USER']
            logged_user = models.User.objects.filter(name=header_request)
            if len(logged_user) < 1:
                response = {'error': 'No existent user provided as session user'}
            else:
                response = func(request, logged_user[0])
        else:
            response = {'error': 'No user provided as session user'}
        return response

    return with_session_decorator
