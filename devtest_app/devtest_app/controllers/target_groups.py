from django.http import JsonResponse, Http404
from main.models import TargetGroup, Country


def index(request, country_code):
    country = Country.objects.filter(country_code=country_code)
    if len(country) == 0:
        return Http404()

    if request.user.is_authenticated:
        target_groups = TargetGroup.objects.filter(external_id=country[0]).values()
    else:
        target_groups = TargetGroup.objects.filter(external_id=country[0]).values("id", "name", "external_id",
                                                                                  "panel_provider_id", "parent_id")

    return JsonResponse({"targetGroups": list(target_groups)})
