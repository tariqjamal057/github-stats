"""Django template tags for rendering form fields with consistent styling.

This module provides template tags to render form fields with customizable CSS classes and styling
options for labels, errors, and help text.
"""

from django import template

register = template.Library()


@register.inclusion_tag("partials/form/field.html")
def render_form_field(
    field,
    field_type,
    placeholder="",
    field_class="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm"
    "focus:outline-none focus:ring-green-900 focus:border-green-900",
    label_class="block text-sm font-medium text-gray-700",
    error_class="text-red-700 text-sm",
    help_text_class="text-gray-400 text-sm",
):  # pylint: disable=too-many-arguments
    """Render a form field with consistent styling and customizable CSS classes.

    Args:
        field: The form field to render
        field_type: The type of field (e.g., 'text', 'email', 'password')
        placeholder (str, optional): Placeholder text for the field. Defaults to "".
        field_class (str, optional): CSS classes for the field input. Defaults to Tailwind classes.
        label_class (str, optional): CSS classes for the field label. Defaults to Tailwind classes.
        error_class (str, optional): CSS classes for error messages. Defaults to Tailwind classes.
        help_text_class (str, optional): CSS classes for help text. Defaults to Tailwind classes.

    Returns:
        dict: Context dictionary containing field and styling information
    """
    return {
        "field": field,
        "field_type": field_type,
        "placeholder": placeholder,
        "field_class": field_class,
        "label_class": label_class,
        "error_class": error_class,
        "help_text_class": help_text_class,
    }
