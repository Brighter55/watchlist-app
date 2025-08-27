from django.http import JsonResponse
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
