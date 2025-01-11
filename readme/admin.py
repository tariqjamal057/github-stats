"""Admin interface configuration for readme models."""

from django.contrib import admin
from unfold.admin import ModelAdmin

from readme.models import Column, Group


@admin.register(Column)
class ColumnAdmin(ModelAdmin):
    """Admin interface for Column model."""

    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    """Admin interface for Group model."""

    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
