from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from charts.views import StationView, station_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StationView.as_view(), name = 'stations'),
    path('chart/<int:pk>/', station_detail, name = 'charts')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]