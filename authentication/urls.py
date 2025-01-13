"""URL configuration for the readme application.

This module defines the URL patterns for routing requests to appropriate views.
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from authentication.views import RegisterView
from core.constant import AUTHENTICATION_APP_NAME

app_name = AUTHENTICATION_APP_NAME

urlpatterns = [
    path("login", LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register", RegisterView.as_view(), name="register"),
]
