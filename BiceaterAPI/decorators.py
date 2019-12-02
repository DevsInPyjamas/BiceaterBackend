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


def check_authorized(func):
    def check_authorized_decorator(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)
        response = func(request, *args, **kwargs)

        return response

    return check_authorized_decorator
