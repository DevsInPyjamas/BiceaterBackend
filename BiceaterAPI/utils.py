import requests
import json

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden


def datos_abiertos():
    response = requests.get(
        'https://datosabiertos.malaga.eu/recursos/transporte/EMT/EMTocupestacbici/ocupestacbicifiware.json')
    malaga = response.content
    return json.loads(malaga)


def check_authorized(user):
    if not user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)


def throw_bad_request():
    error_str = {'error': 'BAD REQUEST:  It is required to receive an argument'}
    return HttpResponseBadRequest(json.dumps(error_str))


def throw_forbidden():
    return HttpResponseForbidden()


def find_station_by_id():
    pass