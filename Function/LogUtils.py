import os
import logging
import logging.handlers


__all__ = ["logger"]

# 用户配置部分 ↓
LEVEL_COLOR = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}
STDOUT_LOG_FMT = "%(log_color)s[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s"
STDOUT_DATE_FMT = "%Y-%m-%d %H:%M:%S"
FILE_LOG_FMT = "[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s"
FILE_DATE_FMT = "%Y-%m-%d %H:%M:%S"


# 用户配置部分 ↑

class ColoredFormatter(logging.Formatter):
    COLOR_MAP = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
    }

    def __init__(self, fmt, date_fmt):
        super().__init__(fmt, date_fmt)

    def parse_color(self, level_name):
        color_name = LEVEL_COLOR.get(level_name, "")
        if not color_name:
            return ""

        color_value = []
        color_name = color_name.split(",")
        for _cn in color_name:
            color_code = self.COLOR_MAP.get(_cn, "")
            if color_code:
                color_value.append(color_code)

        return "\033[" + ";".join(color_value) + "m"

    def format(self, record):
        record.log_color = self.parse_color(record.levelname)
        message = super(ColoredFormatter, self).format(record) + "\033[0m"

        return message


def _get_logger(log_to_file=True, log_filename="default.log", log_level="DEBUG"):
    _logger = logging.getLogger(__name__)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(
        ColoredFormatter(
            fmt=STDOUT_LOG_FMT,
            date_fmt=STDOUT_DATE_FMT,
        )
    )
    _logger.addHandler(stdout_handler)

    if log_to_file:
        _tmp_path = os.path.dirname(os.path.abspath(__file__))
        _tmp_path = os.path.join(_tmp_path, "../logs/{}".format(log_filename))
        file_handler = logging.handlers.TimedRotatingFileHandler(_tmp_path, when="midnight", backupCount=30,
                                                                 encoding="utf-8")
        file_formatter = logging.Formatter(
            fmt=FILE_LOG_FMT,
            datefmt=FILE_DATE_FMT,
        )
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)

    _logger.setLevel(log_level)
    return _logger


logger = _get_logger(log_to_file=True)

