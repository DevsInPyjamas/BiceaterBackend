from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
# Create your views here.

from django.core.paginator import Paginator

from .models import *
import json
from .decorators import returns_json, check_authorized
from .utils \
    import datos_abiertos, throw_bad_request, \
    throw_forbidden, general_info_from_station, \
    to_dict_auth_user, unique_entries
from haversine import haversine
from django.http import HttpResponse
import re


# READ OPERATIONS

@check_authorized
@returns_json
def all_users(request):
    if request.method == 'GET' and 'user_input' in request.GET:
        user_input = request.GET.get("user_input", '')
        user_set = User.objects.filter(username__contains=user_input)
        emails_set = User.objects.filter(email__contains=user_input)
        response = []
        for user in user_set:
            to_dict_auth_user(response, user)
        for user_email in emails_set:
            to_dict_auth_user(response, user_email)
        return unique_entries(response)
    else:
        query_response = User.objects.all()
        dict_response = {}
        [to_dict_auth_user(dict_response, i) for i in query_response]
        return dict_response


@check_authorized
@returns_json
def users_by_id(request, user_id):
    if user_id:
        user = AppUser.objects.get(user_id=user_id)
        query_response = AppUser.objects.get(user=user)
        dicted_response = [query_response.to_dict()]
        return dicted_response
    else:
        throw_bad_request()


@check_authorized
@returns_json
def all_comments(request):
    query_response = Comment.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


@returns_json
def logout(request):
    user = getattr(request, 'user', None)
    if not getattr(user, 'is_authenticated', True):
        user = None
    request.session.flush()
    return {"message": "okey"}


@check_authorized
@returns_json
def comments_by_user_id(request, user_id):
    if user_id:
        comments = Comment.objects.filter(author=user_id).order_by('-date')
        taking_by_page = int(request.GET.get('taking'))
        paginator = Paginator(comments, taking_by_page)
        page = int(request.GET.get('page'))

        comments_page = paginator.get_page(page)
        comments_page_response = [i.to_dict() for i in comments_page.object_list]
        return {"comments": comments_page_response, "count": paginator.count}
    else:
        throw_bad_request()


@returns_json
def comments_by_station_id(request, station_id):
    if station_id:
        comments = Comment.objects.filter(bike_hire_docking_station_id=station_id).order_by('-date')
        taking_by_page = int(request.GET.get('taking'))
        paginator = Paginator(comments, taking_by_page)
        page = int(request.GET.get('page'))

        comments_page = paginator.get_page(page)
        comments_page_response = [i.to_dict() for i in comments_page.object_list]
        return {"comments": comments_page_response, "count": paginator.count}
    else:
        throw_bad_request()


@check_authorized
@returns_json
def one_comment_by_user_id(request, user_id, comment_id):
    if user_id and comment_id:
        query_response = Comment.objects.filter(author=AppUser.objects.get(user_id=user_id), comment_id=comment_id)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


@check_authorized
@returns_json
def me(request):
    return {"id": request.user.appuser.user_id}


@returns_json
def comment_by_stop(request, stop_input):
    stop_input = None
    if request.method == 'GET' and 'stop_input' in request.GET:
        stop_input = request.GET.get("stop_input", '')
    if stop_input:
        query_response = Comment.objects.filter(bike_hire_docking_station_id=stop_input)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


@check_authorized
@returns_json
def comment_of_comment(request, comment_id):
    if comment_id:
        query_response = Comment.objects.filter(comment_id=comment_id)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


# CREATE OPERATIONS
@csrf_exempt
@check_authorized
def create_comment(request):
    body = json.loads(request.body.decode('utf-8'))
    text = None
    bike_hire_docking_station_id = None
    comment_id = None
    if request.method == 'POST' and 'comment' in body:
        text = body['comment']
        if bike_hire_docking_station_id in body and comment_id in body:
            throw_bad_request()
        elif bike_hire_docking_station_id in body:
            bike_hire_docking_station_id = body['bikeDockingStationId']
        elif comment_id in body:
            comment_id = body['commentId']
        else:
            throw_bad_request()
    if text and (bike_hire_docking_station_id or comment_id):
        comment = Comment()
        comment.text = text
        comment.bike_hire_docking_station_id = bike_hire_docking_station_id
        comment.answers_to = comment_id
        author = AppUser.objects.get(user=request.user.id)
        comment.author = author
        comment.save()
        return HttpResponse(content="Comment Created", status=HTTPStatus.OK)
    else:
        throw_bad_request()


@csrf_exempt
@check_authorized
def update_user(request):
    app_user = AppUser.objects.get_or_create(user=request.user)
    body = json.loads(request.body.decode('utf-8'))
    username = None
    first_name = None
    last_name = None
    genre = None
    dob = None
    description = None
    hobbies = None
    if (request.method == 'POST' and 'username' in body and 'name' in body
            and 'surname' in body and 'gender' in body and 'birthDate' in body
            and 'bio' in body and 'hobbies' in body):
        username = body['username']
        first_name = body['name']
        last_name = body['surname']
        genre = body['gender']
        dob = body['birthDate']
        description = body['bio']
        hobbies = body['hobbies']
    if username and first_name and last_name and genre and dob and description and hobbies:
        request.user.username = username
        request.user.first_name = first_name
        request.user.last_name = last_name
        app_user.genre = genre
        app_user.DoB = dob
        app_user.description = description
        app_user.hobbies = hobbies
        request.user.save()
        app_user.save()
        return HttpResponse(content="Comment Created", status=HTTPStatus.OK)
    else:
        throw_bad_request()


@check_authorized
def delete_comment(request):
    comment_id = None
    if request.method == 'POST' and 'comment_id' in request.POST:
        comment_id = request.POST['comment_id']
    if comment_id:
        comment = Comment.objects.get(comment_id=comment_id)
        user = AppUser.objects.get(user=request.user)
        if comment.author == user:
            comment.delete()
        else:
            throw_forbidden()
    else:
        throw_bad_request()


@check_authorized
def delete_user(request):
    request.user.delete()


# FETCH API DATOS ABIERTOS

# @check_authorized
@returns_json
def fetch_stations(request):
    stations_json = datos_abiertos()
    stations = []
    for element in stations_json:
        location = element['location']['value']
        address = element['address']['value']
        address['streetAddress'] = re.sub(r'[_]+', ' ', element['address']['value']['streetAddress'])
        station_id = element['id'].split(':')[3]
        stations.append({station_id: [location, address]})
    return stations


@returns_json
def fetch_station(request, station_id):
    stations_json = datos_abiertos()
    output_dict = [element for element in stations_json if element['id'].split(':')[3] == station_id]
    output_dict = output_dict[0]
    output_dict['address']['value']['streetAddress'] = \
        re.sub(r'[_]+', ' ', output_dict['address']['value']['streetAddress'])
    output_dict['id'] = output_dict['id'].split(':')[3]
    return output_dict


@csrf_exempt
@returns_json
def calculate_best_route(request):
    location = json.loads(request.body)['currentLocation']
    stations_json = datos_abiertos()
    distance_position = {}
    for element in stations_json:
        station_location = element['location']['value']['coordinates']
        distance_position[element['id']] = haversine(
                (float(location[0]), float(location[1])),
                (float(station_location[0]), float(station_location[1]))
            )

    best_distance = sorted(distance_position.values())[0]
    best_distance_key = None
    for identifier, distance in distance_position.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if distance == best_distance:
            best_distance_key = identifier

    temp = [element for element in stations_json if element['id'] == best_distance_key][0]

    return general_info_from_station(temp)
