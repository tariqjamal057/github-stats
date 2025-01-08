"""This module contains views for rendering the home page of the application."""

from django.views.generic import TemplateView


class Home(TemplateView):
    """A class-based view that renders the home page template.

    Attributes:
        template_name (str): The name of the template to be rendered.
    """

    template_name = "index.html"
