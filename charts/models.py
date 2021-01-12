from django.db import models
from django.utils.safestring import mark_safe
from .utils import UploadTo


class Station(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField(default=True)
    logo_path = models.ImageField(upload_to=UploadTo('logo'), blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def thumbnail_logo(self):
        if self.logo_path:
            return mark_safe('<img src="{url}" width="{width}" />'.format(
                url=self.logo_path.url,
                width=300,
            ))
        else:
            return 'NO IMAGE'
    thumbnail_logo.short_description = 'Thumbnail logo'

    class Meta:
        verbose_name_plural = 'Stations'
        verbose_name = 'Station'

    def __str__(self):
        return self.name


class Chart(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    data = models.JSONField()
    added_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Charts'
        verbose_name = 'Chart'
        unique_together = ('station', 'added_date')

    def __str__(self):
        return self.station.name
