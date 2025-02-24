"""This module contains the constant values used accross the project."""

from django.db import models

# Readme APP name
README_APP_NAME = "readme"

# Authentication App name
AUTHENTICATION_APP_NAME = "auth"

# readme build types
README_BUILD_TYPES = [
    {
        "icon": "fa-solid fa-arrows-up-down-left-right",
        "title": "Drag & Drop Builder",
        "description": "Build your README from scratch using our intuitive drag-and-drop "
        "interface with live preview.",
        "action_name": "Try Builder",
        "url": f"{README_APP_NAME}:home",
    },
    {
        "icon": "fa-solid fa-copy",
        "title": "Clone Templates",
        "description": "Start with pre-built templates designed for different project types "
        "and customize them to your needs.",
        "action_name": "Explore Templates",
        "url": f"{README_APP_NAME}:home",
    },
]


class ColumnBuildType(models.TextChoices):
    """Text choices defining the types of column builds available.

    Choices:
        USER: Column created by a user
        DEFAULT: System default column
    """

    USER = "user", "User"
    DEFAULT = "default", "Default"
