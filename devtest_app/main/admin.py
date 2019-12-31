from django.contrib import admin
from .models import LocationGroup, Country, PanelProvider, Location, TargetGroup

# Register your models here.
admin.site.register(LocationGroup)
admin.site.register(Country)
admin.site.register(PanelProvider)
admin.site.register(Location)
admin.site.register(TargetGroup)
