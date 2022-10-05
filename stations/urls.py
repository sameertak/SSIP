from django.urls import path, include, re_path
from .views import AddStation, GetStationNameById, GetAllSubdivisions, GetAllDistrict

urlpatterns = [
    re_path('add/', AddStation.as_view()),
    re_path('get/', GetStationNameById.as_view()),
    re_path('districts/get', GetAllDistrict.as_view()),
    re_path('sub-division/get', GetAllSubdivisions.as_view()),
]