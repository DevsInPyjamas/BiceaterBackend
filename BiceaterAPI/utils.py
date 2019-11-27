import requests
import json


def datos_abiertos():
    response = requests.get(
        'https://datosabiertos.malaga.eu/recursos/transporte/EMT/EMTocupestacbici/ocupestacbicifiware.json')
    malaga = response.content
    return json.loads(malaga)
