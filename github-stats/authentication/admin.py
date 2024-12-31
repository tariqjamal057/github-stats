"""Admin interface configuration for authentication models.

This module customizes the admin interface for User and Group models using Django's admin framework
with Unfold UI enhancements.
"""

from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)


# pylint: disable = unnecessary-pass
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    """Custom admin interface for User model.

    Extends both BaseUserAdmin and Unfold's ModelAdmin to provide enhanced UI features while
    maintaining core user management functionality.
    """

    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    """Custom admin interface for Group model.

    Extends both BaseGroupAdmin and Unfold's ModelAdmin to provide enhanced UI features while
    maintaining core group management functionality.
    """

    compressed_fields = True
    warn_unsaved_form = True
