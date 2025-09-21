from django.http import JsonResponse
from django.conf import settings
import json
from django.apps import apps
from .models import Watchlist, Watching, Watched
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SignUp
from django.contrib.auth.models import User

@api_view(["POST"])
@permission_classes([AllowAny])
def get_users(request):
    users = []
    for user in User.objects.all():
        users.append({"id": user.id, "username": user.username})
    return Response({"users": users})


@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def watchlist(request): # handle fetch from React and return all of the movies' title in database
    data = json.loads(request.body)
    owner = int(data["owner"])
    user_id = request.user.id
    if request.user.is_authenticated and user_id == owner:
        movies = []
        for movie in Watchlist.objects.all():
            if movie.user_id == user_id:
                movies.append({"title": movie.title, "id": movie.id, "user_id": movie.user_id})
        return Response({"movies": movies})
    else:
        movies = []
        for movie in Watchlist.objects.all():
            if movie.user_id == owner:
                movies.append({"title": movie.title, "id": movie.id, "user_id": movie.user_id})
        return Response({"movies": movies})

@api_view(["POST"])
@permission_classes([IsAuthenticated])  # Only logged in users
def watchlist_add(request):
    # check for access token in headers->Authorization
    # store in postgresDB
    data = json.loads(request.body)
    owner = int(data["owner"])
    title = data["movieName"]
    user_id = request.user.id
    if user_id != owner:  # check if authorized user is adding a movie in their table
        return Response({"error": "This is not your table!"})
    username = request.user.username
    movie = Watchlist(title=title, user_id=user_id)
    movie.save()
    return Response({"success": f"{movie} has been added to {username}'s database and his user id is {user_id}"})

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def watching(request):
    data = json.loads(request.body)
    owner = int(data["owner"])
    user_id = request.user.id
    if request.user.is_authenticated and user_id == owner:
        movies = []
        for movie in Watching.objects.all():
            if movie.user_id == user_id:
                movies.append({"title": movie.title, "id": movie.id, "user_id": movie.user_id})
        return Response({"movies": movies})
    else:
        movies = []
        for movie in Watching.objects.all():
            if movie.user_id == owner:
                movies.append({"title": movie.title, "id": movie.id, "user_id": movie.user_id})
        return Response({"movies": movies})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_add_movie(request):
    # check if authorized user is in their table
    data = json.loads(request.body)
    owner = int(data["owner"])
    if request.user.id != owner:
        return Response({"error": "This is not your table"}, status=400)
    # delete movie from "from" database
    movie = json.loads(request.body)
    model_name = movie["from"]
    app_name = "api"
    DeletedModelClass = apps.get_model(app_name, model_name)
    deleted_movie = DeletedModelClass.objects.get(id=movie["id"])
    deleted_movie.delete()
    # Add movie from "to" to database
    model_name = movie["to"]
    AddedModelClass = apps.get_model(app_name, model_name)
    added_movie = AddedModelClass(title=movie["title"], user_id=movie["user_id"])
    added_movie.save()
    return Response({"success": f"Movie--{movie['title']}--has been deleted from api_{movie['from'].lower()} and added to api_{movie['to'].lower()}"})

@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def watched(request):
    data = json.loads(request.body)
    owner = int(data["owner"])
    user_id = request.user.id
    if request.user.is_authenticated and user_id == owner:
        movies = []
        for movie in Watched.objects.all():
            if movie.user_id == user_id:
                movies.append({"title": movie.title, "id": movie.id, "user_id": movie.user_id})
        return Response({"movies": movies})
    else:
        movies = []
        for movie in Watched.objects.all():
            if movie.user_id == owner:
                movies.append({"title": movie.title, "id": movie.id, "user_id": movie.user_id})
        return Response({"movies": movies})

@api_view(["POST"])
@permission_classes([AllowAny])
def sign_up(request):
    new_user = json.loads(request.body)
    serializer = SignUp(data=new_user)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"success": f"{user.username} is now a user"})
    return Response({"error": f"{user.username} is not yet a user"})

#subclass of TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        response = super().post(request)  # {"access": ..., "refresh": ...}
        data = response.data
        access = data["access"]
        refresh = data["refresh"]
        res = Response({"access": access})
        res.set_cookie(
            key="refresh_token",
            value=refresh,
            httponly=True,
            secure=False, # True when deployed
            samesite="None"
            # max_age=60 * 60 * 24 * 7 for refresh to last 7 days
        )
        return res

