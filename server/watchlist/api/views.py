from django.http import JsonResponse
from django.conf import settings
import json
from datetime import datetime, timedelta
import jwt


def watchlist_add(request):
    if request.method == "POST":
        # send response back to React
    return JsonResponse({"error": "Invalid method"})

def get_JWT_token(request):
    if request.method == "POST":
        payload = {
            "anon": True,
            "exp": datetime.now() + timedelta(hours=1)
            "iat": datetime.now()
        }
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        return JsonResponse({"token": token})
    return JsonResponse({"error": "Invalid method"})
