from .views import form
from django.urls import path

urlpatterns = [
    path("form/", form.as_view(), name="Feedback Form"),
]