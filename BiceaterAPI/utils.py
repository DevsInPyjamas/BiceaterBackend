import requests
import json
import re

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


def general_info_from_station(datos_abiertos):
    return {
        "location":
            datos_abiertos['location']['value']['coordinates'],
        "direction":
            re.sub(r'[_]+', ' ', datos_abiertos['address']['value']['streetAddress']),
        "id":
            datos_abiertos['id'].split(':')[3],
        "totalSlotNumber":
            datos_abiertos['totalSlotNumber']['value'],
        "freeSlotNumber":
            datos_abiertos['freeSlotNumber']['value'],
        "availableBikeNumber":
            datos_abiertos['availableBikeNumber']['value']
    }


def to_dict_auth_user(response_dict, user):
    response_dict[user.id] = {
        "username": user.username,
        "id": user.id,
        "email": user.email
    }
