from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Stations'
        verbose_name = 'Station'

    def __str__(self):
        return self.name


class Chart(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    data = models.TextField(null=False, blank=False)
    added_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Charts'
        verbose_name = 'Chart'
        unique_together = ('station', 'added_date')

    def __str__(self):
        return self.station.name