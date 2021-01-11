from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from charts.views import StationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StationView.as_view(), name = 'stations')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]