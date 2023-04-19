import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from location.models import Location


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def send_location(request):
    data = json.loads(request.body)

    location = Location.objects.create(lat=data["lat"], long=data["long"])
    location.save()
    response = {"error": None, "data": location.lat, "success": True}

    return JsonResponse(response)


def get_location(request):
    location = Location.objects.latest('created_on')
    response = {"error": None, "data": [location.lat, location.long], "success": True}
    return JsonResponse(response)