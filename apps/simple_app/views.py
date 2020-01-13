from django.shortcuts import HttpResponse


def get_messages(request):
    return HttpResponse("OK")