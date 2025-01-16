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
    list_display = ["id", "name", "symbol", "icon", "type", "build_type"]
    list_display_links = ["id", "name"]
    list_filter = ["type", "build_type"]
    search_fields = ["name", "symbol", "type", "build_type"]
    fields = [
        "name",
        "symbol",
        "icon",
        "description",
        "type",
        "build_type",
        "created_by",
        "deleted_at",
        "restored_at",
    ]


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    """Admin interface for Group model."""

    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ["id", "name", "build_type"]
    list_display_links = ["id", "name"]
    list_filter = ["build_type"]
    search_fields = ["name"]
    fields = [
        "name",
        "icon",
        "description",
        "columns",
        "build_type",
        "created_by",
        "deleted_at",
        "restored_at",
    ]
