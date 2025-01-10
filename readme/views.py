"""This module contains views for rendering the home page of the application."""

from django.views.generic import TemplateView

from core import constant


class Home(TemplateView):
    """A class-based view that renders the home page template.

    Attributes:
        template_name (str): The name of the template to be rendered.
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the template.

        Returns:
            dict: The context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["build_types"] = constant.README_BUILD_TYPES
        return context
