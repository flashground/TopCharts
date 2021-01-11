from django.shortcuts import render
from django.views.generic import ListView
from .models import Station, Chart
import json


class StationView(ListView):
    queryset = Station.objects.filter(active=True)
    model = Station
    template_name = 'charts/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     chart = Chart.objects.all().first()
    #     json_text = chart.data[:5]
    #     chart_list = []
    #     for json in json_text:
    #         chart_list.append(f"{json['singer']} - {json['song']}")
    #     context['date'] = chart.added_date
    #     context['chart'] = chart_list
    #     a=5

        # return context
    
