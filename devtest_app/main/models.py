from django.db import models
from django.core.exceptions import ValidationError


class Country(models.Model):
    country_code = models.TextField(max_length=3)
    panel_provider_id = models.ForeignKey("PanelProvider", on_delete=models.CASCADE)  # check on delete

    def __str__(self):
        return self.country_code


class Location(models.Model):
    name = models.TextField(max_length=50)
    external_id = models.ManyToManyField("LocationGroup")
    secret_code = models.TextField()

    def __str__(self):
        return self.name


class LocationGroup(models.Model):
    name = models.TextField(max_length=50)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)  # check on delete
    panel_provider_id = models.ForeignKey("PanelProvider", on_delete=models.CASCADE)  # check on delete

    def __str__(self):
        return self.name


class PanelProvider(models.Model):
    code = models.CharField(choices=(("L", "LetterProvider"), ("A", "ArrayProvider"), ("N", "NodeProvider")),
                            max_length=50)

    def __str__(self):
        return self.code


class TargetGroup(models.Model):
    name = models.TextField(max_length=50)
    external_id = models.ManyToManyField(Country)
    panel_provider_id = models.ForeignKey(PanelProvider, on_delete=models.CASCADE)  # check on delete
    parent_id = models.ForeignKey("TargetGroup", on_delete=models.CASCADE, null=True, default=None,
                                  blank=True)  # check on delete
    secret_code = models.TextField()

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent_id is not None and self.externail_id is not None:
            raise ValidationError("Country can be set only if target group is root")
