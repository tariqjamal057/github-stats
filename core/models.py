"""Core models module containing base model classes for the application.

Provides common fields and functionality for model inheritance.
"""

from django.db import models
from django_softdelete.models import SoftDeleteModel


class BaseModel(SoftDeleteModel):
    """Abstract base model class that provides common timestamp fields and soft delete
    functionality.

    Inherits from SoftDeleteModel to enable soft deletion instead of permanent deletion.
    All models in the application should inherit from this class to maintain consistency.

    Attributes:
        created_at (DateTimeField): Timestamp when the record was created
        updated_at (DateTimeField): Timestamp when the record was last updated
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for model configuration."""

        abstract = True
