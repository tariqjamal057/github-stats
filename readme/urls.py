"""URL configuration for the readme application.

This module defines the URL patterns for routing requests to appropriate views.
"""

from django.urls import path

from core.constant import README_APP_NAME
from readme.views import index

app_name = README_APP_NAME

urlpatterns = [
    path("", index.Home.as_view(), name="home"),
]
