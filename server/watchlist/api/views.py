from django.http import JsonResponse
from django.conf import settings
import json
from datetime import datetime, timedelta
import jwt


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
                movie = json.loads(request.body)["movieName"]
                return JsonResponse({"success": f"Movie--{movie}--has been added to the database"})
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
