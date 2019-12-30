from django.http import HttpResponse


def index(request, country_code):
    return HttpResponse("country_code: " + country_code)
