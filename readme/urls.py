"""URL configuration for the readme application.

This module defines the URL patterns for routing requests to appropriate views.
"""

from django.urls import path

from readme import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]
