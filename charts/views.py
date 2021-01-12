from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Station, Chart


class StationView(ListView):
    queryset = Station.objects.filter(active=True)
    model = Station
    template_name = 'charts/index.html'


def station_detail(request, pk):
    object_ = Chart.objects.filter(station_id=pk)
    return render(request, 'charts/chart.html', {'object':object_})