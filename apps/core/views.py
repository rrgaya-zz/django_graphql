from django.http import JsonResponse
from .schema import schema



def index(request):
    context = schema.execute()
    return JsonResponse(context.data, safe=False)