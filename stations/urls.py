from django.urls import path, include
from .views import Stations

urlpatterns = [
    path('^get_data/(?P<username>.+)/$', Stations.as_view(), name="Filter Parameters"),
]