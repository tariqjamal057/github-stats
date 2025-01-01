"""Authentication application configuration module.

This module contains the configuration class for the authentication app, defining core settings
like the database field type and app name.
"""

from django.apps import AppConfig


# pylint: disable = unnecessary-pass
class AuthenticationConfig(AppConfig):
    """Configuration class for the authentication application.

    Attributes:
        default_auto_field (str): The default primary key field type for models
        name (str): The name of the application
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
