from django.http import JsonResponse

def watchlist_add(request):
    if request.method == "POST":
        try:
            data = json.load(request.body)
            print(data)
            return JsonResponse({"success": f"Success the data in python object is {data}"}, status=200)
    return JsonResponse({"error": "Error in watchlist_add: Only POST required"}, status=405)
