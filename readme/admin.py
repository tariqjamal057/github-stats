"""Admin interface configuration for readme models."""

from django.contrib import admin
from unfold.admin import ModelAdmin

from readme.models import Component, ReadmeData, Section


@admin.register(Component)
class ComponentAdmin(ModelAdmin):
    """Admin interface for Component model."""

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


@admin.register(Section)
class SectionAdmin(ModelAdmin):
    """Admin interface for Section model."""

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


@admin.register(ReadmeData)
class ReadmeDataAdmin(ModelAdmin):
    """Admin interface for ReadmeData model."""

    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ["id", "file_name", "build_type"]
    list_display_links = ["id", "file_name"]
    list_filter = ["build_type"]
    search_fields = ["file_name"]
    fields = [
        "file_name",
        "build_type",
        "data",
        "created_by",
        "deleted_at",
        "restored_at",
    ]
