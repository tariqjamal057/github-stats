"""Readme Application.

This module contains the configuration class for the readme app, defining core settings like the
database field type and app name.
"""

from django.apps import AppConfig


class ReadmeConfig(AppConfig):
    """Configuration class for the readme application.

    Attributes:
        default_auto_field (str): The default primary key field type for models
        name (str): The name of the application
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "readme"
