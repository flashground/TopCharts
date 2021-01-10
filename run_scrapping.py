import os, sys

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


def main():
    for station in STATIONS_LIST:
        if check_station(station[0])[1]:
            chart_data = station[1].main()
            chart = Chart(data = chart_data[0]['chart'],
                          added_date = chart_data[0]['date'],
                          station_id=Station.objects.filter(slug=station[0]).first())
        else:
            pass


if __name__ == "__main__":
    main()