import logging
import os
from enum import Enum


class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def get_logger(name: str, level: LogLevel = LogLevel.INFO) -> logging.Logger:
    if isinstance(level, str):
        try:
            level = LogLevel[level.upper()]
        except KeyError:
            raise ValueError(
                f"Invalid log level '{level}'. Choose from: {', '.join(l.name for l in LogLevel)}"
            )

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler()
    logger.setLevel(level.value)
    formatting = logging.Formatter(
        "[%(asctime)s] - %(levelname)s::%(name)s - %(message)s"
    )
    handler.setFormatter(formatting)
    logger.addHandler(handler)

    return logger
