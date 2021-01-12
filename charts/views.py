from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework import permissions

from .models import Station, Chart
from .serializers import StationSerializer, ChartSerializer


class StationView(ListView):
    queryset = Station.objects.filter(active=True)
    model = Station
    template_name = 'charts/index.html'


def station_detail(request, pk):
    object_ = Chart.objects.filter(station_id=pk)
    return render(request, 'charts/chart.html', {'object':object_})


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all().order_by('-id')
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all().order_by('-id')
    serializer_class = ChartSerializer
    permission_classes = [permissions.IsAuthenticated]