from enum import Enum


class LogFormat(str, Enum):
    """Presets for logging formats that can be used in :func:`.set_log`.

    ``{color}`` and ``{end}`` are used to add the default color of the current log level.
    Specific colors like ``{red}`` and ``{green}`` can also be used.

    If no colors are used, the whole log message will be colored.

    ``//`` at the end of the log format is used to indicate that new lines will be fully colored.
    """

    full_color = "[%(levelname)s] %(message)s"
    full_color_time = "[%(asctime)s] %(levelname)s: %(message)s"
    color_level = "[{color}%(levelname)s{end}] %(message)s"
    color_level_time = "[{color}%(asctime)s{end}] [{color}%(levelname)s{end}] %(message)s"
    colorful = "{magenta}[%(asctime)s]{end} - {cyan}%(levelname)s{end} | %(message)s"
    default = "[{color}%(levelname)s{end}] %(message)s//"

    def __str__(self):
        return self.value


class TimeFormat(str, Enum):
    """Presets for the time format that is used in :func:`.set_log`."""

    datetime = "%Y-%m-%d %H:%M:%S"
    time = "%H:%M:%S"
    default = "%H:%M:%S"

    def __str__(self):
        return self.value


class ReadyEvent(Enum):
    """Styles for the ready event."""

    box = 0
    box_colorful = 1
    box_bold = 2
    logs = 3
    table = 4
    table_bold = 5
    table_vertical = 6
    table_vertical_bold = 7
    default = table

    def __str__(self):
        return self.name
