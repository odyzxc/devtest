from django.http import JsonResponse, Http404
from main.models import Location, LocationGroup, Country


def index(request, country_code):
    country = Country.objects.filter(country_code=country_code)
    if len(country) == 0:
        return Http404()
    location_ids = LocationGroup.objects.values_list('location').filter(country_id=country[0])

    if request.user.is_authenticated:
        locations = Location.objects.filter(id__in=location_ids).values()
    else:
        locations = Location.objects.filter(id__in=location_ids).values("id", "name")

    # public API
    return JsonResponse({"locations": list(locations)})
