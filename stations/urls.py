from django.urls import path, include, re_path
from .views import AddStation, GetStationNameById

urlpatterns = [
    re_path('add/', AddStation.as_view()),
    re_path('get/', GetStationNameById.as_view()),
]