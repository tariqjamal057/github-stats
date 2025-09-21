"""Models module for managing README data.

Defines the data structure for customizable columns and their groupings.
"""

from django.db import models

from core.constant import ColumnBuildType
from core.models import BaseModel


class ReadmeData(BaseModel):
    """Model represents the data for readme display

    Attributes:
        file_name (str): Name of the readme file
        build_type (str): Type of column build (user/default)
        data (json): Data of the data readme file
        created_by (User): Reference to the user who created the column
    """

    file_name = models.CharField(max_length=50)
    build_type = models.CharField(
        max_length=20,
        choices=ColumnBuildType.choices,
        default=ColumnBuildType.USER,
        db_default=ColumnBuildType.DEFAULT,
    )
    data = models.JSONField(null=True, default=list)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        """Meta class for model configuration."""

        db_table = "readme_datas"

    def __str__(self):
        """Returns string representation of the Column.

        Returns:
            str: The name of the column
        """
        return str(self.file_name)
