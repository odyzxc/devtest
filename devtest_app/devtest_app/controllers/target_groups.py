from django.http import HttpResponse


def index(request, country_code):
    return HttpResponse("Country code: " + country_code)
