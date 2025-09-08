from django.http import JsonResponse
from django.conf import settings
import json
from datetime import datetime, timedelta
import jwt
from django.apps import apps
from .models import Watchlist, Watching, Watched

def watchlist(request): # handle fetch from React and return all of the movies' title in database
    if request.method == "POST":
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing header or Invalid token"}, status=401)
        token = auth_header.replace("Bearer ", "")
        try:
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            if data.get("anon"):  # if the token is for anonymous
                movies = []
                for movie in Watchlist.objects.all():
                    movies.append({"title": movie.title, "id": movie.id})
                return JsonResponse({"movies": movies})
            else:
                return JsonResponse({"error": "The token is not for anonymous users"}, status=403)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "The token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

    return JsonResponse({"error": "Invalid method"}, status=405)

def watchlist_add(request):
    if request.method == "POST":
        # send response back to React
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing header or Invalid token"}, status=401)
        token = auth_header.replace("Bearer ", "")
        try:
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            if data.get("anon"):  # if the token is for anonymous
                # store in postgresDB
                title = json.loads(request.body)["movieName"]
                movie = Watchlist(title=title)
                movie.save()
                return JsonResponse({"success": f"Movie--{title}--has been added to the database"})
            else:
                return JsonResponse({"error": "The token is not for anonymous users"}, status=403)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "The token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

    return JsonResponse({"error": "Invalid method"}, status=405)

def watching(request):
    if request.method == "POST":
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing header or Invalid token"}, status=401)
        token = auth_header.replace("Bearer ", "")
        try:
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            if data.get("anon"):  # if the token is for anonymous
                movies = []
                for movie in Watching.objects.all():
                    movies.append({"title": movie.title, "id": movie.id})
                return JsonResponse({"movies": movies})
            else:
                return JsonResponse({"error": "The token is not for anonymous users"}, status=403)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "The token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

    return JsonResponse({"error": "Invalid method"}, status=405)

def delete_add_movie(request):
    if request.method == "POST":
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing header or Invalid token"}, status=401)
        token = auth_header.replace("Bearer ", "")
        try:
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            if data.get("anon"):
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
            else:
                return JsonResponse({"error": "The token is not for anonymous users"}, status=403)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "The token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)
    return JsonResponse({"error": "Invalid method"}, status=405)

def watched(request):
    if request.method == "POST":
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing header or Invalid token"}, status=401)
        token = auth_header.replace("Bearer ", "")
        try:
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            if data.get("anon"):  # if the token is for anonymous
                movies = []
                for movie in Watched.objects.all():
                    movies.append({"title": movie.title, "id": movie.id})
                return JsonResponse({"movies": movies})
            else:
                return JsonResponse({"error": "The token is not for anonymous users"}, status=403)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "The token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)
    return JsonResponse({"error": "Invalid method"}, status=405)

def get_JWT_token(request):
    if request.method == "POST":
        payload = {
            "anon": True,
            "exp": datetime.utcnow() + timedelta(seconds=3600),
            "iat": datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        return JsonResponse({"token": token})
    return JsonResponse({"error": "Invalid method"}, status=405)
