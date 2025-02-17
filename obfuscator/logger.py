import logging
import os


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        if os.getenv("DEBUG", "FALSE").upper() == "TRUE":
            log_level = logging.DEBUG
        else:
            log_level = logging.INFO

        logger.setLevel(log_level)

        handler = logging.StreamHandler()
        formatting = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        handler.setFormatter(formatting)

        logger.addHandler(handler)

    return logger
