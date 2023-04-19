from django.http import JsonResponse


def json_success(data):
    return JsonResponse({"error": None, "data": data, "success": True})


def json_error(error, status=400):
    return JsonResponse({"error": error, "data": None, "success": False}, status=status)

