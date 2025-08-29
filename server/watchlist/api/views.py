from django.http import JsonResponse
from django.middleware.csrf import get_token
import json


def watchlist_add(request):
    if request.method == "POST":
        try:
            data = json.load(request.body)
            print(data)
            return JsonResponse({"success": f"Success the data in python object is {data}"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Error in watchlist_add: Only POST required"}, status=405)

def get_CSRF_token(request):
    return JsonResponse({"success": "CSRF token set!", "csrftoken": get_token(request)})
