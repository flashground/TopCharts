from rest_framework import serializers
from .models import Station, Chart


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class ChartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chart
        fields = ['id', 'station', 'added_date', 'created_date', 'updated_date', 'data']
