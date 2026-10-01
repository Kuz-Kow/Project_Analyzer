import logging
from logging.handlers import RotatingFileHandler
from config.setting import DEFAULT_LOG_FILE


def set_logger() -> None:
    """
    Sets logger to write INFO messages and above to a file and print WARNING message and above to console
    """

    logger = logging.getLogger()
    logger.setLevel("INFO")
    file_formatter = logging.Formatter(
        fmt="{asctime} - {name} - {levelname}: {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    cls_formatter = logging.Formatter(fmt="{name} - {levelname}: {message}", style="{")

    file_handler = RotatingFileHandler(
        filename=DEFAULT_LOG_FILE,
        mode="a",
        maxBytes=1000,
        backupCount=10,
        encoding="utf-8",
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel("INFO")
    logger.addHandler(file_handler)

    cls_handler = logging.StreamHandler()
    cls_handler.setFormatter(cls_formatter)
    cls_handler.setLevel("ERROR")
    logger.addHandler(cls_handler)
