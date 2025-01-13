"""Module for handling user authentication views in the application.

This module provides views for user registration and authentication functionality.
"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from github_stats import settings


class RegisterView(CreateView):
    """View for handling user registration.

    Extends Django's CreateView to provide user registration functionality. Uses the default
    UserCreationForm and redirects to login page on successful registration.
    """

    template_name = "auth/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy(settings.LOGIN_URL)
