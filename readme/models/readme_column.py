"""Models module for managing README columns and groups configuration.

Defines the data structure for customizable columns and their groupings.
"""

from django.db import models
from django.utils.html import format_html

from core.constant import ColumnBuildType
from core.models import BaseModel


class ColumnIcons(models.TextChoices):
    """Text s defining the available icons for columns."""

    HEADING = "fa-solid fa-heading", "Heading"
    PARAGRAPH = "fa-solid fa-paragraph", "Paragraph"
    LIST = "fa-solid fa-list", "List"
    CHECK = "fa-solid fa-check", "Check"
    UNORDERED_LIST = "fa-solid fa-list-ul", "Unordered List"
    ORDERED_LIST = "fa-solid fa-list-ol", "Ordered List"
    BLOCK_QUOTE = "fa-solid fa-quote-left", "Block Quote"
    CODE = "fa-solid fa-code", "Code"
    MULTILINE_CODE = "fa-solid fa-code-branch", "Multiline Code"
    HORIZONTAL_RULE = "fa-solid fa-grip-horizontal", "Horizontal Rule"
    ITALIC = "fa-solid fa-italic", "Italic"
    BOLD = "fa-solid fa-bold", "Bold"
    STRIKETHROUGH = "fa-solid fa-strikethrough", "Strikethrough"
    UNDERLINE = "fa-solid fa-underline", "Underline"
    LINK = "fa-solid fa-link", "Link"
    IMAGE = "fa-solid fa-image", "Image"
    VIDEO = "fa-solid fa-video", "Video"
    AUDIO = "fa-solid fa-music", "Audio"
    TABLE = "fa-solid fa-table", "Table"
    TASK_LIST = "fa-solid fa-list-check", "Task List"
    ESCAPING = "fa-solid fa-exclamation-triangle", "Escaping"
    FOOTNOTES = "fa-solid fa-quote-right", "Footnotes"


class IconChoices(models.TextChoices):
    """Enumeration defining the available icons for columns."""

    USER = "fa-solid fa-user", "User"
    USERS = "fa-solid fa-users", "Users"
    HEART = "fa-solid fa-heart", "Heart"
    STAR = "fa-solid fa-star", "Star"
    BELL = "fa-solid fa-bell", "Bell"
    ENVELOPE = "fa-solid fa-envelope", "Envelope"
    CALENDAR = "fa-solid fa-calendar", "Calendar"
    COG = "fa-solid fa-cog", "Cog"
    HOME = "fa-solid fa-home", "Home"
    SEARCH = "fa-solid fa-search", "Search"
    TRASH = "fa-solid fa-trash", "Trash"
    EDIT = "fa-solid fa-edit", "Edit"
    DOWNLOAD = "fa-solid fa-download", "Download"
    UPLOAD = "fa-solid fa-upload", "Upload"
    CAMERA = "fa-solid fa-camera", "Camera"
    FILE = "fa-solid fa-file", "File"
    LOCK = "fa-solid fa-lock", "Lock"
    UNLOCK = "fa-solid fa-unlock", "Unlock"
    PLUS = "fa-solid fa-plus", "Plus"
    MINUS = "fa-solid fa-minus", "Minus"
    CHECK = "fa-solid fa-check", "Check"
    TIMES = "fa-solid fa-times", "Times"
    EXCLAMATION = "fa-solid fa-exclamation", "Exclamation"
    QUESTION = "fa-solid fa-question", "Question"
    INFO = "fa-solid fa-info", "Info"
    WRENCH = "fa-solid fa-wrench", "Wrench"
    CLOUD = "fa-solid fa-cloud", "Cloud"
    DOWNLOAD_CLOUD = "fa-solid fa-cloud-download-alt", "Cloud Download"
    UPLOAD_CLOUD = "fa-solid fa-cloud-upload-alt", "Cloud Upload"
    GLOBE = "fa-solid fa-globe", "Globe"
    FOLDER = "fa-solid fa-folder", "Folder"
    FOLDER_OPEN = "fa-solid fa-folder-open", "Folder Open"
    CHART_BAR = "fa-solid fa-chart-bar", "Bar Chart"
    CHART_LINE = "fa-solid fa-chart-line", "Line Chart"
    COMMENT = "fa-solid fa-comment", "Comment"
    COMMENTS = "fa-solid fa-comments", "Comments"
    PHONE = "fa-solid fa-phone", "Phone"
    TABLE = "fa-solid fa-table", "Table"
    TAG = "fa-solid fa-tag", "Tag"
    TAGS = "fa-solid fa-tags", "Tags"
    TOOLS = "fa-solid fa-tools", "Tools"
    USER_CIRCLE = "fa-solid fa-user-circle", "User Circle"
    USER_CHECK = "fa-solid fa-user-check", "User Check"
    USER_PLUS = "fa-solid fa-user-plus", "User Plus"
    USER_MINUS = "fa-solid fa-user-minus", "User Minus"
    USER_TIMES = "fa-solid fa-user-times", "User Times"


class ColumnType(models.TextChoices):
    """Text choices defining the types of columns available."""

    BASIC = "basic", "Basic"
    COMPONENT = "component", "Component"


class ColumnSymbol(models.TextChoices):
    """Text choices defining the symbols for columns."""

    # basic elements
    HEADING_1 = "#", "Heading 1"
    HEADING_2 = "##", "Heading 2"
    HEADING_3 = "###", "Heading 3"
    HEADING_4 = "####", "Heading 4"
    HEADING_5 = "#####", "Heading 5"
    HEADING_6 = "######", "Heading 6"
    PARAGRAPH = "", "Paragraph"
    UNORDERED_LIST_TYPE_1 = "-", "Unordered List (-)"
    UNORDERED_LIST_TYPE_2 = "*", "Unordered List (*)"
    UNORDERED_LIST_TYPE_3 = "+", "Unordered List (+)"
    ORDERED_LIST = "1.", "Ordered List"
    BLOCKQUOTE = ">", "Block Quote"
    # advanced elements
    CODE = "code", "Code"
    MULTILINE_CODE = "multiline_code", "Multiline Code"
    HORIZONTAL_RULE = "---", "Horizontal Rule"
    ITALIC = "italic", "Italic"
    BOLD = "bold", "Bold"
    STRIKETHROUGH = "strikethrough", "Strikethrough"
    UNDERLINE = "underline", "Underline"
    LINK = "link", "Link"
    IMAGE = "image", "Image"
    VIDEO = "video", "Video"
    AUDIO = "audio", "Audio"
    TABLE = "table", "Table"
    TASK_LIST = "task_list", "Task List"
    ESCAPING = "escaping", "Escaping"
    FOOTNOTES = "footnotes", "Footnotes"


class Component(BaseModel):
    """Model representing a configurable component in the README display.

    Attributes:
        name (str): Display name of the component
        symbol (str): Short symbol/identifier for the component
        icon (str): Icon associated with the component
        description (str): Detailed description of the component's purpose
        type (str): Type of component (basic/component)
        build_type (str): Type of component build (user/default)
        created_by (User): Reference to the user who created the component
    """

    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50, choices=ColumnSymbol.choices)
    icon = models.CharField(
        max_length=50,
        choices=ColumnIcons.choices,
        default=ColumnIcons.HEADING,
        db_default=ColumnIcons.HEADING,
    )
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=20,
        choices=ColumnType.choices,
        default=ColumnType.BASIC,
        db_default=ColumnType.BASIC,
    )
    build_type = models.CharField(
        max_length=20,
        choices=ColumnBuildType.choices,
        default=ColumnBuildType.USER,
        db_default=ColumnBuildType.DEFAULT,
    )
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        """Meta class for model configuration."""

        db_table = "components"

    def __str__(self):
        """Returns string representation of the Component.

        Returns:
            str: The name of the components
        """
        return str(self.name)

    @property
    def icon_tag(self):
        """Generates HTML tag for the group's icon.

        Returns:
            str: HTML string containing FontAwesome icon markup
        """
        return format_html(f'<i class="{self.icon}"></i>')


class Section(BaseModel):
    """Model representing a sections of related columns.

    Attributes:
        name (str): Name of the column sections
        icon (str): Icon associated with the sections
        description (str): Detailed description of the sections's purpose
        columns (ManyToManyField): Collection of columns in this sections
        build_type (str): Type of sections build (user/default)
        created_by (User): Reference to the user who created the sections
    """

    name = models.CharField(max_length=255)
    icon = models.CharField(
        max_length=50,
        choices=IconChoices.choices,
        default=IconChoices.FOLDER,
        db_default=IconChoices.FOLDER,
    )
    description = models.TextField(null=True, blank=True)
    columns = models.ManyToManyField(Component)
    build_type = models.CharField(
        max_length=20,
        choices=ColumnBuildType.choices,
        default=ColumnBuildType.USER,
        db_default=ColumnBuildType.DEFAULT,
    )
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        """Meta class for model configuration."""

        db_table = "sections"

    def __str__(self):
        """Returns string representation of the Group.

        Returns:
            str: The name of the group
        """
        return str(self.name)

    @property
    def icon_tag(self):
        """Generates HTML tag for the group's icon.

        Returns:
            str: HTML string containing FontAwesome icon markup
        """
        return f'<i class="{self.icon}"></i>'
