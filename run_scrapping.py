import os, sys

from charts.parsers import europa_plus, loveradio
from charts.models import Station, Chart


project_path = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'top_charts.settings'

import django
django.setup()


def main():
    europa_plus()
    loveradio()

if __name__ == "__main__":
    main()