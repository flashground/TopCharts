from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework import routers

from charts.views import StationView, station_detail, StationViewSet, ChartViewSet


router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'charts', ChartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StationView.as_view(), name='stations'),
    path('chart/<int:pk>/', station_detail, name='charts'),
    path('api/', include(router.urls)),
    # path('restapi/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
