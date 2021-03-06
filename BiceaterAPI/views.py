from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
# Create your views here.

from django.core.paginator import Paginator

from .models import *
import json
from .decorators import returns_json, check_authorized, cross_origin
from .utils \
    import datos_abiertos, throw_bad_request, \
    throw_forbidden, general_info_from_station, \
    to_dict_auth_user, unique_entries
from haversine import haversine
from django.http import HttpResponse
import re


# READ OPERATIONS

@cross_origin
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


@cross_origin
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


@cross_origin
@check_authorized
@returns_json
def all_comments(request):
    query_response = Comment.objects.all()
    dicted_response = [i.to_dict() for i in query_response]
    return dicted_response


@cross_origin
@returns_json
def logout(request):
    user = getattr(request, 'user', None)
    if not getattr(user, 'is_authenticated', True):
        user = None
    request.session.flush()
    return {"message": "okey"}


@cross_origin
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


@cross_origin
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


@cross_origin
@check_authorized
@returns_json
def one_comment_by_user_id(request, user_id, comment_id):
    if user_id and comment_id:
        query_response = Comment.objects.filter(author=AppUser.objects.get(user_id=user_id), comment_id=comment_id)
        dicted_response = [i.to_dict() for i in query_response]
        return dicted_response
    else:
        throw_bad_request()


@cross_origin
@check_authorized
@returns_json
def me(request):
    return {"id": request.user.appuser.user_id}


@cross_origin
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


@cross_origin
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
@cross_origin
@check_authorized
@returns_json
def create_comment(request):
    body = json.loads(request.body.decode('utf-8'))
    text = None
    bikeDockingStationId = None
    comment_id = None
    if request.method == 'POST' and 'comment' in body:
        text = body['comment']
        if 'bikeDockingStationId' in body and 'comment_id' in body:
            bikeDockingStationId = body['bikeDockingStationId']
            comment_id = body['comment_id']
        elif 'bikeDockingStationId' in body:
            bikeDockingStationId = body['bikeDockingStationId']
        elif 'comment_id' in body:
            comment_id = body['comment_id']
        else:
            throw_bad_request()
    if text and (bikeDockingStationId or comment_id):
        comment = Comment()
        comment.text = text
        comment.bike_hire_docking_station_id = bikeDockingStationId
        comment.answers_to_id = comment_id
        author = None
        try:
            author = AppUser.objects.get(user=request.user.id)
        except Exception:
            author = AppUser()
            author.user = User.objects.get(id=request.user.id)
            author.save()
        comment.author = author
        comment.save()
        return {"ok": "ok"}
    else:
        throw_bad_request()


@csrf_exempt
@cross_origin
@check_authorized
@returns_json
def create_rating(request):
    body = json.loads(request.body.decode('utf-8'))
    rating = None
    author = request.user.appuser
    station_id = None
    if request.method == 'POST' and 'rating' in body and 'station_id' in body:
        rating = body['rating']
        station_id = body['station_id']
    if rating and author and station_id:
        rating_object = Rating()
        rating_object.rating = rating
        rating_object.author = author
        rating_object.bike_hire_docking_station_id = station_id
        rating_object.save()
        return {'ok': 'ok'}
    else:
        throw_bad_request()


@csrf_exempt
@cross_origin
@check_authorized
@returns_json
def update_user(request):
    body = json.loads(request.body.decode('utf-8'))
    if (request.method == 'POST' and 'userId' in body and 'username' in body and 'name' in body
            and 'surname' in body and 'gender' in body and 'birthDate' in body
            and 'bio' in body and 'hobbies' in body):
        user_id = body['userId']
        username = body['username']
        first_name = body['name']
        last_name = body['surname']
        genre = body['gender']
        dob = body['birthDate']
        description = body['bio']
        hobbies = body['hobbies']
        app_user = AppUser.objects.get_or_create(user_id=user_id)[0]

        user = AppUser.objects.get(user=request.user)

        if user != app_user:
            throw_forbidden()
        else:
            app_user.user.username = username
            app_user.user.first_name = first_name
            app_user.user.last_name = last_name
            app_user.genre = genre
            app_user.DoB = dob
            app_user.description = description
            app_user.hobbies = hobbies
            app_user.user.save()
            app_user.save()
            return {"ok": "ok"}
    else:
        throw_bad_request()


@cross_origin
@check_authorized
@returns_json
def delete_comment(request, comment_id):
    if comment_id:
        comment = Comment.objects.get(comment_id=comment_id)
        user = AppUser.objects.get(user=request.user)
        if comment.author == user or comment.author.isAdmin:
            comment.delete()
        else:
            throw_forbidden()
    else:
        throw_bad_request()
    return {"ok": "ok"}


@cross_origin
@check_authorized
def delete_user(request):
    request.user.delete()


# FETCH API DATOS ABIERTOS

@cross_origin
# @check_authorized
@returns_json
def fetch_stations(request):
    stations_json = datos_abiertos()
    stations = []
    for element in stations_json:
        location = element['location']['value']
        location['coordinates'] = [location['coordinates'][1], location['coordinates'][0]]
        address = element['address']['value']
        address['streetAddress'] = element['address']['value']['streetAddress']
        station_id = element['id'].split('-')[1]
        stations.append({station_id: [location, address]})
    return stations


@cross_origin
@returns_json
def fetch_station(request, station_id):
    stations_json = datos_abiertos()
    output_dict = [element for element in stations_json if element['id'].split('-')[1] == station_id]
    output_dict = output_dict[0]
    output_dict['location']['value']['coordinates'] = [output_dict['location']['value']['coordinates'][1], output_dict['location']['value']['coordinates'][0]]
    output_dict['id'] = output_dict['id'].split('-')[1]
    return output_dict


@csrf_exempt
@cross_origin
@returns_json
def calculate_best_route(request):
    location = json.loads(request.body)['currentLocation']
    stations_json = datos_abiertos()
    distance_position = {}
    for element in stations_json:
        station_location = element['location']['value']['coordinates']
        station_location = [station_location[1], station_location[0]]
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


@csrf_exempt
@cross_origin
@returns_json
def search_station_by_address(request):
    address = json.loads(request.body)['stationAddress']
    stations_json = datos_abiertos()
    stations = [element for element in stations_json if str.lower(element['address']['value']['streetAddress'])
        .__contains__(str.lower(address))]
    for element in stations:
        element['id'] = element['id'].split('-')[1]
    return stations


@csrf_exempt
@cross_origin
@returns_json
def rating_average(request, station_id):
    ratings = Rating.objects.filter(bike_hire_docking_station_id=station_id)
    if station_id and ratings and ratings.count() != 0:
        total = 0
        for rating in ratings:
            total += rating.rating
        return total/ratings.count()
    else:
        return 0


@check_authorized
@returns_json
def comments_parameters(request, comment_id):
    if comment_id:
        query_response = Comment.objects.get(comment_id=comment_id)
        dicted_response = [query_response.to_dict()]
        return dicted_response

    else:
        throw_bad_request()


@check_authorized
@returns_json
def users_parameters(request, string):
    if string:
        user = User.objects.filter(username__icontains=string)
        query_response = AppUser.objects.get(user=user)
        dicted_response = [query_response.to_dict()]
        return dicted_response

    else:
        throw_bad_request()


@check_authorized
@returns_json
def comments_responses(request, comment_id):

    if comment_id:
        bbbb = int(comment_id)
        query_response = Comment.objects.filter(answers_to__comment_id=bbbb).order_by('-date')
        if query_response:
            dicted_response = [i.to_dict() for i in query_response]
            return dicted_response
        else:
            throw_bad_request()
    else:
        throw_bad_request()
