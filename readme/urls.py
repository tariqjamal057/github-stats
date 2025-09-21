"""URL configuration for the readme application.

This module defines the URL patterns for routing requests to appropriate views.
"""

from django.urls import path

from core.constant import README_APP_NAME
from readme.views.index import Home
from readme.views.readme_data import CreateReadmeFile, ReadmeDataView, UpdateReadmeFile

app_name = README_APP_NAME

urlpatterns = [
    path("", Home.as_view(), name="home"),

    # readme file
    path("readme/file/create", CreateReadmeFile.as_view(), name="create_readme_file"),
    path('readme/file/update/<int:id>', UpdateReadmeFile.as_view(), name='update_readme_file'),

    path("readme/file/<int:id>/content/create", ReadmeDataView.as_view(), name="create_readme_data"),
]

