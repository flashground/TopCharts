import os, sys

from django.db import DatabaseError

project_path = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'top_charts.settings'

import django
django.setup()

from charts.parsers import europaplus, loveradio
from charts.models import Station, Chart

STATIONS_LIST = (('europaplus', europaplus),
                 ('loveradio', loveradio))

def check_station(name):
    station = Station.objects.filter(slug=name).first()
    if station:
        return True, bool(station.active)
    return False, False

def save_to_database(station, chart_data):
    chart = Chart(data=chart_data[0]['chart'],
                  added_date=chart_data[0]['date'],
                  station=Station.objects.filter(slug=station[0]).first())
    try:
        chart.save()
    except DatabaseError as e:
        pass

def main():
    for station in STATIONS_LIST:
        if check_station(station[0])[1]:
            chart_data = station[1].main()
            for chart in chart_data:
                if chart[0]:
                    save_to_database(station, chart)
        else:
            pass


if __name__ == "__main__":
    main()