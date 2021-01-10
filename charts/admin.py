from django.contrib import admin
from .models import Chart, Station


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass