from django.http import JsonResponse
from django.conf import settings
import json
from django.apps import apps
from .models import Watchlist, Watching, Watched
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SignUp

def watchlist(request): # handle fetch from React and return all of the movies' title in database
    if request.method == "POST":
        movies = []
        for movie in Watchlist.objects.all():
            movies.append({"title": movie.title, "id": movie.id})
        return JsonResponse({"movies": movies})
    return JsonResponse({"error": "Invalid method"}, status=405)

@api_view(["POST"])
@permission_classes([IsAuthenticated])  # Only logged in users
def watchlist_add(request):
    # check for access token in headers->Authorization
    # store in postgresDB
    data = json.loads(request.body)
    title = data["movieName"]
    user_id = request.user.id
    username = request.user.username
    movie = Watchlist(title=title, user_id=user_id)
    movie.save()
    return Response({"success": f"{movie} has been added to {username}'s database and his user id is {user_id}"})

def watching(request):
    if request.method == "POST":
        movies = []
        for movie in Watching.objects.all():
            movies.append({"title": movie.title, "id": movie.id})
        return JsonResponse({"movies": movies})
    return JsonResponse({"error": "Invalid method"}, status=405)

def delete_add_movie(request):
    if request.method == "POST":
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
        added_movie = AddedModelClass(title=movie["title"])
        added_movie.save()
        return JsonResponse({"success": f"Movie--{movie['title']}--has been deleted from api_{movie['from'].lower()} and added to api_{movie['to'].lower()}"})
    return JsonResponse({"error": "Invalid method"}, status=405)

def watched(request):
    if request.method == "POST":
        movies = []
        for movie in Watched.objects.all():
            movies.append({"title": movie.title, "id": movie.id})
        return JsonResponse({"movies": movies})
    return JsonResponse({"error": "Invalid method"}, status=405)

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

