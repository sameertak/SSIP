from django.urls import path, include
from .views import admin_login

urlpatterns = [
    path("login/<mail>", admin_login.as_view(), name="Admin Login"),
]